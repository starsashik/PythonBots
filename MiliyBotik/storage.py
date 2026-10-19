import json
import os
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile
from config import DATA_DIR, DATA_FILE


def read_data() -> dict:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        return {'users': {}, 'invitations': [], 'next_id': 1}
    with DATA_FILE.open('r', encoding='utf-8') as f:
        data = json.load(f)
    data.setdefault('users', {})
    data.setdefault('invitations', [])
    data.setdefault('next_id', 1)
    return data


def write_data(data: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    # Перезапись через временный файл защищает JSON от частичной записи.
    with NamedTemporaryFile('w', dir=DATA_DIR, encoding='utf-8', delete=False, suffix='.tmp') as f:
        temp_path = Path(f.name)
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temp_path, DATA_FILE)


def bind_user(username: str, user_id: int) -> bool:
    data = read_data()
    old_id = data['users'].get(username)
    # Username — только первоначальное подтверждение. После него ID привязывается.
    if old_id is not None and old_id != user_id:
        return False
    for other, other_id in data['users'].items():
        if other != username and other_id == user_id:
            return False
    data['users'][username] = user_id
    write_data(data)
    return True


def get_partner(username: str, allowed_users: dict) -> str:
    return next(u for u in allowed_users if u != username)


def create_invitation(creator: str, recipient: str, details: dict) -> dict:
    data = read_data()
    invitation = {
        'id': data['next_id'], 'creator': creator, 'recipient': recipient,
        **details, 'status': 'pending',
        'created_at': datetime.now().isoformat(timespec='seconds'),
        'responded_at': None,
    }
    data['next_id'] += 1
    data['invitations'].append(invitation)
    write_data(data)
    return invitation


def get_invitation(invitation_id: int) -> dict | None:
    return next((i for i in read_data()['invitations'] if i['id'] == invitation_id), None)


def nearest_invitation(username: str) -> dict | None:
    now = datetime.now()
    upcoming = [i for i in read_data()['invitations']
                if i['recipient'] == username
                and datetime.fromisoformat(i['datetime']) >= now
                and i['status'] in ('pending', 'accepted')]
    return min(upcoming, key=lambda i: i['datetime'], default=None)


def history(username: str) -> list[dict]:
    return sorted((i for i in read_data()['invitations']
                   if username in (i['creator'], i['recipient'])),
                  key=lambda i: i['datetime'], reverse=True)


def set_response(invitation_id: int, username: str, status: str) -> dict | None:
    if status not in ('accepted', 'declined'):
        return None
    data = read_data()
    for invite in data['invitations']:
        if invite['id'] == invitation_id and invite['recipient'] == username and invite['status'] == 'pending':
            invite['status'] = status
            invite['responded_at'] = datetime.now().isoformat(timespec='seconds')
            write_data(data)
            return invite
    return None


def get_user_id(username: str) -> int | None:
    return read_data()['users'].get(username)
