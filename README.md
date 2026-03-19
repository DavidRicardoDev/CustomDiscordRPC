# Custom Discord RPC

Una aplicación minimalista de escritorio para que personalices tu Rich Presence de Discord a tu antojo. Hecha con **Python** de fondo y **Vue 3 + Tailwind CSS** de frente.

## Características

- Interfaz moderna en Modo Oscuro.
- Totalmente fuera de línea. No usa servidores externos; la aplicación aloja una mini-API interna en tu propia computadora.
- Soporta GIFs e imágenes mediante **URLs** externas. No tienes que subir las imágenes manualmente al Portal de Desarrollador de Discord.
- Totalmente instalable mediante su propio `Custom Discord RPC.exe`.

## Cómo usar el programa pre-compilado

1. Entra a la carpeta `dist`.
2. Dale doble clic al archivo `Custom Discord RPC.exe`. (La primera vez que abra puede demorar un par de segundos mientras extrae los archivos visuales temporalmente).
3. Asegúrate de tener **Discord abierto y ejecutándose** en tu computadora.
4. Escribe tu Client ID (Application ID) que creaste en el Discord Developer Portal.
5. Rellena los detalles, el estado y las imágenes con las URLs que más te gusten, y dale a Actualizar RPC.

### ¿Cómo obtener el Client ID?

1. Entra a [Discord Developer Portal](https://discord.com/developers/applications).
2. Haz clic en **New Application** arriba a la derecha. Ponle el nombre que quieras que tus amigos vean debajo de tu estado "Jugando a ...".
3. Copia el `Application ID` (esa es tu Client ID) y pégala en esta aplicación.

## Para desarrolladores y actualizaciones
Si deseas hacer modificaciones de la interfaz web (Vue), entra a la carpeta `frontend/` y usa el comando `npm install` y `npm run dev`. Alternativamente, utiliza el script `run_dev.bat` incluido en el directorio principal.
Una vez listo, re-compila ejecutando `build_exe.bat`.

---

## 📜 Historial de Versiones (Changelog)

### v1.1.0 
- Añadida guía visual para obtener Client ID en pantalla.
- Panel de historial de versiones (Changelog) emergente.
- Añadidos logos de Python y Vue y reestructura del footer.
- Optimización de caché de WebView2 para desarrolladores.

### v1.0.0 
- Lanzamiento inicial (Release Oficial).
- Diseño profesional (Glassmorphism oscuro).
- Soporte para enlaces URL directos (Imágenes principales).
- Sistema de feedback visual (Toasts).
- Empaquetamiento automatizado y repositorio online.
