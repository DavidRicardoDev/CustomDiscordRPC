# Custom Discord RPC

Una aplicación minimalista de escritorio para que personalices tu Rich Presence de Discord a tu antojo. Hecha con **Python** de fondo y **Vue 3 + CSS Reactivo** de frente.
¡100% Código Abierto (Open Source)! Puedes revisar todo el código fuente y clonar el repositorio tú mismo; nuestra aplicación no lee tokens privados ni maneja datos sensibles, únicamente interactúa con tu ID pública de "Discord Developer".

## Características de la v1.4.0

- 🗂️ **Sistema de Perfiles Predeterminados:** Guarda localmente infinitos estados y configuraciones de Discord en tu PC. Edítalos, personalízalos por nombre y elimínalos en lote.
- 🔁 **Rotación Mágica de `Client ID`:** Si cargas un perfil que contiene un ID (Nombre de Aplicación) distinto, el motor te desconectará del viejo y ejecutará el *handshake* con la nueva App automáticamente en una fracción de segundo.
- 🎨 **Theming Personalizado:** Elige el color que desees (RGB/HEX) mediante la paleta superior. El tema y luces cambiarán al instante en toda la aplicación.
- 📉 **Segundo Plano (System Tray):** Minimiza la app al área del reloj de Windows en lugar de cerrarla. Se despierta con un solo *Left Click*.
- ⏱️ **Tiempo Transcurrido:** Al conectarte, inicia un conteo visible ("00:00 elapsed") en Discord para saber tu tiempo de actividad continuo y real.
- 🖼️ **Imágenes Livianas y Tooltips:** Visualiza tooltips estilo Discord y mantén la aplicación robusta; sin alojar nada pesadamente, todo mediante URLs externas directas.

## Cómo usar el programa pre-compilado

1. Descarga el archivo de la release o dirígete a la carpeta `dist`.
2. Dale doble clic al archivo `Custom Discord RPC.exe`.
   > **⚠️ Nota de Seguridad (Windows Defender / Antivirus):** Como este es un programa compilado y empaquetado por PyInstaller sin un Certificado Digital de paga corporativo, Windows SmartScreen y ciertos antivirus podrían saltar con un **falso positivo** advirtiendo que "se bloqueó una app desconocida". Simplemente presiona **"Más información"** -> **"Ejecutar de todas formas"** (Márcalo como exclusión en otras apps si es necesario). El código de este programa está 100% publicado y a la vista de todos; no hace nada malicioso.
3. Asegúrate de tener **Discord abierto y ejecutándose en segundo plano**.
4. Escribe tu Client ID (Application ID) que creaste en el Discord Developer Portal.
5. Rellena los detalles, el estado y las URLs, y presiona "Actualizar Presencia en Discord" 🚀.

### ¿Cómo obtener el Client ID?

1. Entra a [Discord Developer Portal](https://discord.com/developers/applications).
2. Haz clic en **New Application** arriba a la derecha. Ponle el nombre que quieras que tus amigos vean debajo de tu estado "Jugando a ...".
3. Copia el `Application ID` (esa es tu Client ID) y pégala dentro de este lanzador.

## Actualizaciones Futuras
Como es un programa portable de tipo Ejecutable único (`.exe`), para adquirir o disfrutar de nuevas características de futuras revisiones, simplemente tendrás que volver a descargar la nueva versión desde la pestaña "Releases" de este mismo repositorio GitHub y re-utilizar ese nuevo archivo.

## Para desarrolladores
Si deseas hacer modificaciones de la interfaz web (Vue) a profundidad:
1. Clona el repositorio y entra a la carpeta `frontend/`.
2. Usa el comando `npm install` y posteriormente `npm run dev`. Alternativamente, utiliza el script `run_dev.bat`.
3. Una vez programado, re-compila el ecosistema global ejecutando el batch automatizado `build_exe.bat`.

---

## 📜 Historial de Versiones (Changelog)

### v1.4.0
- **Gran Sistema de Perfiles Predeterminados:** Dashboard integrado para crear, editar y cargar perfiles usando un almacenamiento nativo robusto `profiles.json`.
- **Auto-Reconexión de IDs:** Cambio de Aplicación instantáneo al detectar la carga de un perfil con origen distinto.
- Mejoras de accesibilidad: Auto-cerrado de ventanas al dar click afuera, *Single-Left-Click* en íconos de bandeja para despertar el panel.

### v1.3.1
- Restricción del sistema a 'Instancias Únicas' previniendo que la aplicación se duplique creando procesos fantasmas.
- Mejoras visuales en las cajas de texto invisibles.

### v1.3.0
- Integración de Theming Dinámico Interactivo (Colores modificables a profundidad por el usuario).
- Backend minimizable en System Tray nativo de Windows (Bandeja de sistema Pystray).
- Cronómetro base de Python añadido (Tiempo de Conexión en vivo sumatorio en el Perfil).
- Spinners de petición de red Asíncronos.
- Ejecutable `.exe` con el logo propio y oficial de la Custom App.

### v1.2.0
- Panel "Vista Previa en Vivo" que emula la previsualización nativa del perfil de Discord (Tooltips en Hover).
- Parche Anti-CORS con `no-referrer` para cargar links bloqueados desde IMGur y otros hostings de terceros.

### v1.1.0 
- Añadida guía visual de aplicación nativa.
- Historial de cambios modal y optimizaciones UI menores (Notificaciones Toast).
- Componente Python `pywebview` sin caché local.

### v1.0.0 
- Lanzamiento Oficial. Setup de motor local en Python con Webview Vue 3 compilado por Vite.
