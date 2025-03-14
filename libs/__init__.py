from .http_conn import AsyncHTTP, SyncHTTP
from .remanga import ReManga
def __load_cache(self) -> bool:
    """
    Загружает кэш из файла, если он существует.
    Возвращает True, если кэш был успешно загружен, иначе False.
    """
    # Определяем путь к файлу кэша
    path = self.CACHE_PATH.format(self.username) if self.username else self.CACHE_PATH.format(self.token)
    
    # Проверяем, существует ли файл кэша
    if os.path.exists(path):
        try:
            # Открываем файл и загружаем данные
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                
                # Восстанавливаем состояние объекта из кэша
                self.page = data.get('page', 0)
                self.token = data.get('token', self.token)
                self.headers = data.get('headers', self.headers)
                self.username = data.get('username', self.username)
                self.password = data.get('password', self.password)
                self.user_info = data.get('user_info', {})
                self.viewed_chapters = data.get("viewed", [])
                
                # Возвращаем True, если кэш был успешно загружен
                return True
        except Exception as e:
            # Логируем ошибку, если что-то пошло не так
            logger.error(f"Ошибка при загрузке кэша: {e}")
            return False
    else:
        # Если файл кэша не существует, возвращаем False
        return False