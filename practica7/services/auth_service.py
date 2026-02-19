# services/auth_service.py
from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    role: str = ""

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self):
        self._users = {
         "Admin": {"password": "1234","role": "Admin"},
         "Maestro": {"password": "XYZ","role": "Maestro"},
         "Alumno": {"password": "pokemonxy","role": "Alumno"}
        } 

    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")
        user = self._users.get(username)
        if user and user["password"] == password: 
            return AuthResult(True, "Autenticación exitosa.")
        return AuthResult(False, "Usuario o contraseña incorrectos.")
