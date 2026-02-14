# services/auth_service.py
from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self):
        self._users = {
            "Admin": "1234",
            "Maestro": "abcd",
            "Alumno": "xyz"
        }

    def login(self, username: str, password: str) -> AuthResult:
        username = username.strip()
        password = password.strip()

        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")
        
        if username in self._users and self._users[username] == password:
            return AuthResult(True, "Autenticación exitosa.")
        return AuthResult(False, "Usuario o contraseña incorrectos.")
