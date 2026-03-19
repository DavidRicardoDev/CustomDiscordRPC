<template>
  <div :style="themeStyle" class="min-h-screen bg-gradient-to-br from-gray-900 via-[#1a1c23] to-[#121318] flex flex-col items-center justify-center py-10 relative px-4 font-sans text-gray-100 transition-colors duration-500">
    <Transition name="toast">
      <div v-if="toast.show" :class="['fixed top-6 left-1/2 -translate-x-1/2 px-6 py-3 rounded-xl shadow-2xl font-semibold text-white z-50 flex items-center gap-3 backdrop-blur-md', toast.type === 'success' ? 'bg-emerald-500/90 border border-emerald-400/50' : 'bg-rose-500/90 border border-rose-400/50']">
        <span v-if="toast.type==='success'" class="text-xl">✨</span>
        <span v-else class="text-xl">⚠️</span>
        {{ toast.message }}
      </div>
    </Transition>

    <Transition name="fade">
      <div v-if="showGuideModal || showChangelogModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-md">
        <div class="bg-[#2b2d31] border border-white/10 rounded-2xl shadow-2xl max-w-lg w-full max-h-[85vh] overflow-y-auto relative">
          
          <button @click="showGuideModal=false; showChangelogModal=false" class="absolute top-4 right-4 text-gray-400 hover:text-white bg-white/5 hover:bg-white/10 p-2 rounded-xl transition-colors font-bold h-8 w-8 flex items-center justify-center">
            X
          </button>

          <!-- Guide Content -->
          <div v-if="showGuideModal" class="p-8">
            <h2 class="text-2xl font-bold text-white mb-4">¿Dónde obtener tu Client ID?</h2>
            <ol class="list-decimal list-outside ml-4 space-y-4 text-sm text-gray-300">
              <li>Ingresa al <a href="https://discord.com/developers/applications" target="_blank" class="text-blue-400 hover:underline">Discord Developer Portal</a> en tu navegador.</li>
              <li>Haz clic en el botón azul <strong>"New Application"</strong>.</li>
              <li>Ponle el nombre que quieras a tu aplicación (Ese nombre será el que aparecerá luego del "Jugando a..." en tu perfil y <strong>sólo se puede cambiar ahí</strong>).</li>
              <li>Copia el <strong>APPLICATION ID</strong> (Client ID).</li>
              <li>Pega esos números en esta aplicación. ¡Listo!</li>
            </ol>
            <div class="mt-6 rounded-lg bg-[#1e1f22] p-4 text-center border border-dashed border-gray-600">
              <span class="text-gray-500 text-xs uppercase tracking-widest font-bold block mb-2">[Captura de guía]</span>
              <div class="w-full relative aspect-video bg-gray-800 rounded flex flex-col items-center justify-center text-gray-500 text-sm overflow-hidden">
                <img src="./assets/guide.png" class="absolute inset-0 w-full h-full object-cover" @error="$event.target.style.display='none'" />
              </div>
            </div>
          </div>

          <!-- Changelog Content -->
          <div v-if="showChangelogModal" class="p-8">
            <h2 class="text-2xl font-bold text-white mb-6 flex items-center gap-3">📜 Historial de Cambios</h2>
            <div class="space-y-6">
              <div v-for="log in changelog" :key="log.version" class="border-l-2 border-[var(--theme-color)] pl-4 py-1">
                <div class="flex items-end gap-3 mb-2">
                  <h3 class="text-lg font-bold text-[var(--theme-light)]">{{ log.version }}</h3>
                  <span class="text-xs text-gray-400 font-medium mb-0.5">{{ log.date }}</span>
                </div>
                <ul class="list-disc list-inside space-y-1 text-sm text-gray-300">
                  <li v-for="change in log.changes" :key="change">{{ change }}</li>
                </ul>
              </div>
            </div>
            
            <div class="mt-8 bg-blue-500/10 border border-blue-500/20 rounded-xl p-4 flex gap-3 items-start">
              <span class="text-xl">💡</span>
              <p class="text-xs text-blue-200 leading-relaxed pt-1">
                <strong>Actualizaciones:</strong> Por ahora, la aplicación debe descargarse manual desde GitHub para actualizar.
              </p>
            </div>
          </div>

        </div>
      </div>
    </Transition>

    <div class="max-w-5xl w-full bg-[#2b2d31]/80 backdrop-blur-xl border border-white/10 p-8 sm:p-10 rounded-3xl shadow-2xl relative overflow-hidden mt-4">
      <!-- Luces de fondo adaptables al tema -->
      <div class="absolute top-0 right-0 -mr-20 -mt-20 w-64 h-64 rounded-full bg-[var(--theme-color)] opacity-20 blur-3xl pointer-events-none transition-colors duration-500"></div>
      <div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-64 h-64 rounded-full bg-blue-500 opacity-10 blur-3xl pointer-events-none transition-colors duration-500"></div>

      <div class="relative z-10">
        <h1 class="text-3xl sm:text-4xl font-extrabold text-center mb-2 tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-[var(--theme-light)] via-white to-gray-400 transition-colors duration-500 pb-1">
          Presencia de discord personalizada
        </h1>
        
        <div class="flex items-center justify-center gap-3 mb-8 text-xs font-semibold">
          <label class="flex items-center gap-2 text-gray-400 bg-black/20 p-2 rounded-xl border border-white/5 cursor-pointer hover:bg-black/30 transition-colors">
            🎨 Color de Tema
            <input type="color" v-model="userColor" class="w-6 h-6 rounded cursor-pointer border-none p-0 bg-transparent">
          </label>
        </div>

        <div v-if="!connected" class="space-y-6 max-w-sm mx-auto mt-4 animate-fade-in">
          <div class="space-y-2">
            <div class="flex justify-between items-center px-1">
              <label class="block text-sm font-semibold text-gray-300">Client ID (Application ID)</label>
              <button @click="showGuideModal = true" class="text-xs text-[var(--theme-light)] hover:brightness-125 font-bold transition-all flex items-center gap-1 hover:underline underline-offset-2">
                ¿Dónde encontrar esto?
              </button>
            </div>
            <input v-model="form.client_id" type="text" class="w-full bg-[#1e1f22] border border-white/5 rounded-xl px-4 py-3.5 outline-none focus:ring-2 focus:ring-[var(--theme-color)] focus:border-transparent transition-all text-white placeholder-gray-500 shadow-inner" placeholder="Ej: 123456789012345678">
          </div>
          
          <button @click="connect" :disabled="isLoading" class="w-full bg-[var(--theme-color)] hover:brightness-110 py-3.5 rounded-xl text-white font-bold transition-all transform hover:-translate-y-0.5 shadow-lg flex justify-center items-center gap-2">
            <svg v-if="isLoading" class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            <span v-else>Conectar Perfil</span>
          </button>
        </div>

        <div v-else class="animate-fade-in mt-4">
          
          <div class="flex flex-col sm:flex-row justify-between items-center bg-[#1e1f22]/80 border border-white/5 p-4 rounded-2xl gap-4 mb-6">
            <div class="flex items-center gap-3">
              <span class="relative flex h-3 w-3">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
              </span>
              <span class="font-medium text-emerald-400">Enlazado a Discord Exitosamente</span>
            </div>
            
            <div class="flex items-center gap-4">
              <!-- Background minimize toggle -->
              <label class="flex items-center gap-2 cursor-pointer text-xs text-gray-300 hover:text-white transition-colors group">
                <input type="checkbox" v-model="minimizeToTray" @change="updateTraySetting" class="w-4 h-4 rounded text-[var(--theme-color)] bg-[#111214] border-white/10 focus:ring-0 focus:ring-offset-0 cursor-pointer">
                Ejecutar en Segundo Plano
              </label>

              <button @click="disconnect" class="text-rose-400 hover:text-rose-300 text-sm font-semibold transition-colors bg-rose-500/10 hover:bg-rose-500/20 px-4 py-2 rounded-lg">
                Desconectar
              </button>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-5 gap-8">
            
            <!-- FORMULARIO IZQUIERDA -->
            <div class="lg:col-span-3 space-y-6">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                <div class="space-y-1.5">
                  <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Detalles (Details)</label>
                  <input v-model="rpc.details" type="text" class="w-full bg-[#1e1f22] border border-white/5 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[var(--theme-color)] transition-all text-sm text-gray-100 placeholder-gray-600 shadow-inner" placeholder="Ej: Explorando mazmorras...">
                </div>
                <div class="space-y-1.5">
                  <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Estado (State)</label>
                  <input v-model="rpc.state" type="text" class="w-full bg-[#1e1f22] border border-white/5 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[var(--theme-color)] transition-all text-sm text-gray-100 placeholder-gray-600 shadow-inner" placeholder="Ej: Nivel 100">
                </div>
              </div>

              <div class="bg-[#1e1f22]/50 p-5 rounded-2xl border border-white/5 space-y-4 relative group">
                <h3 class="text-sm font-bold text-gray-300 border-b border-gray-700/50 pb-2">🖼️ Imagen Principal (Grande)</h3>
                <div class="hidden group-hover:block absolute top-4 right-4 bg-[var(--theme-dark)] text-xs px-3 py-2 rounded shadow-xl max-w-xs z-20">
                  ⚠️ El enlace debe terminar en <strong>.png, .jpg o .gif</strong> directamente. No servirá el enlace genérico de un post o sitio web.
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                  <div class="space-y-1.5">
                    <label class="block text-xs font-semibold text-gray-400 ml-1">Enlace directo a Imagen</label>
                    <input v-model="rpc.large_image" type="text" class="w-full bg-[#2b2d31] rounded-lg px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-[var(--theme-color)] transition-all text-sm text-gray-200 placeholder-gray-600 border border-transparent focus:border-[var(--theme-color)]" placeholder="https://i.imgur.com/foto.png">
                  </div>
                  <div class="space-y-1.5">
                    <label class="block text-xs font-semibold text-gray-400 ml-1">Texto al pasar el mouse</label>
                    <input v-model="rpc.large_text" type="text" class="w-full bg-[#2b2d31] rounded-lg px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-[var(--theme-color)] transition-all text-sm text-gray-200 placeholder-gray-600 border border-transparent focus:border-[var(--theme-color)]" placeholder="Logo de mi servidor">
                  </div>
                </div>
              </div>

              <div class="bg-[#1e1f22]/50 p-5 rounded-2xl border border-white/5 space-y-4 relative group">
                <h3 class="text-sm font-bold text-gray-300 border-b border-gray-700/50 pb-2">⭐ Imagen Secundaria (Pequeña)</h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                  <div class="space-y-1.5">
                    <label class="block text-xs font-semibold text-gray-400 ml-1">Enlace directo a Imagen</label>
                    <input v-model="rpc.small_image" type="text" class="w-full bg-[#2b2d31] rounded-lg px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-[var(--theme-color)] transition-all text-sm text-gray-200 placeholder-gray-600 border border-transparent focus:border-[var(--theme-color)]" placeholder="https://i.imgur.com/icono.gif">
                  </div>
                  <div class="space-y-1.5">
                    <label class="block text-xs font-semibold text-gray-400 ml-1">Texto al pasar el mouse</label>
                    <input v-model="rpc.small_text" type="text" class="w-full bg-[#2b2d31] rounded-lg px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-[var(--theme-color)] transition-all text-sm text-gray-200 placeholder-gray-600 border border-transparent focus:border-[var(--theme-color)]" placeholder="Rango Administrador">
                  </div>
                </div>
              </div>
              
              <button @click="updateRPC" :disabled="isLoading" class="flex justify-center items-center gap-2 w-full bg-[var(--theme-color)] hover:brightness-110 active:brightness-90 py-4 mt-2 rounded-xl text-white font-extrabold text-lg transition-all transform hover:-translate-y-0.5 shadow-xl">
                <svg v-if="isLoading" class="animate-spin h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                <span v-else>🚀 Actualizar Presencia en Discord</span>
              </button>
            </div>

            <!-- VISTA PREVIA DERECHA -->
            <div class="lg:col-span-2">
              <div class="sticky top-10">
                <h3 class="text-sm font-bold text-gray-300 uppercase tracking-widest mb-4">👀 Vista Previa en Vivo</h3>
                
                <div class="bg-[#111214] p-5 rounded-2xl text-gray-200 font-sans shadow-xl border border-white/10 relative">
                  <h4 class="text-xs font-extrabold text-gray-500 uppercase tracking-widest mb-4">Jugando a un juego</h4>
                  <div class="flex gap-4 items-start">
                    
                    <div class="relative shrink-0">
                      <!-- Imagen grande -->
                      <img v-if="rpc.large_image" :src="rpc.large_image" referrerpolicy="no-referrer"
                           :title="rpc.large_text || ''"
                           class="w-[84px] h-[84px] rounded-xl object-cover bg-gray-800 shadow shadow-black/50" 
                           @error="$event.target.src='https://placehold.co/100x100/2b2d31/4a4d53?text=?'"/>
                      <div v-else class="w-[84px] h-[84px] rounded-xl bg-[#2b2d31] border border-white/5 flex items-center justify-center">
                        <span class="text-4xl">🎮</span>
                      </div>
                      
                      <!-- Imagen pequeña circular -->
                      <img v-if="rpc.small_image" :src="rpc.small_image" referrerpolicy="no-referrer"
                           :title="rpc.small_text || ''"
                           class="w-[30px] h-[30px] rounded-full border-[3px] border-[#111214] absolute -bottom-1 -right-1 bg-gray-800 object-cover" 
                           @error="$event.target.src='https://placehold.co/40x40/2b2d31/4a4d53?text=?'"/>
                    </div>

                    <div class="flex-1 flex flex-col justify-start">
                      <div class="relative group cursor-help inline-block w-fit">
                        <h5 class="text-[15px] font-bold leading-tight mb-1 max-w-[200px] text-[var(--theme-light)] flex items-center gap-1">
                          [Tu Application ID] <span class="text-xs text-gray-500">ⓘ</span>
                        </h5>
                        <div class="hidden group-hover:block absolute top-6 left-0 min-w-[220px] max-w-[260px] bg-[#40444b] text-gray-100 text-xs px-3 py-2 rounded shadow-2xl z-50 border border-[#2b2d31] leading-relaxed">
                          La integración API no puede sobreescribir el nombre central.<br><br>Para cambiar este nombre, debes ir al <strong>Discord Developer Portal</strong> y renombrar tu aplicación padre propiamente.
                        </div>
                      </div>
                      <p class="text-[13px] text-gray-300 leading-snug truncate max-w-[200px]">{{ rpc.details || 'Tus detalles aquí...' }}</p>
                      <p class="text-[13px] text-gray-300 leading-snug truncate max-w-[200px]">{{ rpc.state || 'Tu estado aquí...' }}</p>
                      <p class="text-[12px] text-[var(--theme-light)] mt-1.5 font-bold tracking-wide flex items-center gap-1 opacity-80">
                        00:00 transcurrido
                      </p>
                    </div>
                  </div>
                </div>
                
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="mt-8 mb-2 z-10 flex flex-col items-center">
      <p class="text-gray-400 text-sm font-medium tracking-wide mb-3">
        Creado por <span class="font-bold text-[var(--theme-light)]">ShyLuns</span> (David Peña)
      </p>

      <div class="flex items-center gap-2 px-4 py-2 bg-[#2b2d31]/50 border border-white/5 rounded-full shadow-inner mb-3 transition-colors hover:bg-[#2b2d31]/80">
        <span class="text-xs text-gray-500 font-bold uppercase tracking-widest pl-1">Desarrollado con</span>
        <svg class="h-4 w-4 text-[#3776AB] hover:scale-110 transition-transform" viewBox="0 0 448 512" fill="currentColor">
           <path d="M439.8 200.5c-7.7-30.9-22.3-54.2-53.4-54.2h-40.1v47.4c0 36.8-31.2 67.8-66.8 67.8H172.7c-29.2 0-53.4 25-53.4 54.3v101.8c0 29 25.2 46 53.4 54.3 33.8 9.9 66.3 11.7 106.8 0 26.9-7.8 53.4-23.5 53.4-54.3v-40.7H226.2v-13.6h160.2c31.1 0 42.6-21.7 53.4-54.2 11.2-33.5 10.7-65.7 0-108.6zM286.2 404c11.1 0 20.1 9.1 20.1 20.3 0 11.3-9 20.4-20.1 20.4-11 0-20.1-9.2-20.1-20.4 .1-11.3 9.1-20.3 20.1-20.3zM167.8 248.1h106.8c29.7 0 53.4-25 53.4-54.3V91.9c0-29-24.4-50.7-53.4-55.6-35.8-5.9-74.7-5.6-106.8 .1-45.2 8-53.4 24.7-53.4 55.6v40.7h106.9v13.6h-147c-31.1 0-58.3 18.7-66.8 54.2-9.8 40.7-10.2 66.1 0 108.6 7.6 31.6 25.7 54.2 56.8 54.2H101v-48.8c0-35.3 30.5-66.4 66.8-66.4zm-6.7-142.6c-11.1 0-20.1-9.1-20.1-20.3 .1-11.3 9-20.4 20.1-20.4 11 0 20.1 9.2 20.1 20.4s-9 20.3-20.1 20.3z"/>
        </svg>
        <span class="text-gray-600 font-bold">&amp;</span>
        <svg class="h-4 w-4 text-[#4FC08D] hover:scale-110 transition-transform" viewBox="0 0 448 512" fill="currentColor">
           <path d="M244.6 92.4h119.3L224 332 84.1 92.4H0L224 480 448 92.4H329.4L224 274.5z"/>
        </svg>
      </div>

      <button @click="showChangelogModal = true" class="text-xs text-gray-500 hover:text-[var(--theme-light)] transition-colors underline decoration-gray-700 underline-offset-4 inline-block font-semibold">
        Versión {{ currentVersion }} - Ver Registro de Cambios
      </button>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

function adjustColor(hex, amount) {
  let r = parseInt(hex.substring(1,3), 16);
  let g = parseInt(hex.substring(3,5), 16);
  let b = parseInt(hex.substring(5,7), 16);
  r = Math.max(0, Math.min(255, r + amount));
  g = Math.max(0, Math.min(255, g + amount));
  b = Math.max(0, Math.min(255, b + amount));
  return `#${(r.toString(16).padStart(2,'0'))}${(g.toString(16).padStart(2,'0'))}${(b.toString(16).padStart(2,'0'))}`;
}

const userColor = ref(localStorage.getItem('rpc_theme') || '#6366f1')
const themeStyle = ref({})

watch(userColor, (val) => {
  themeStyle.value = {
    '--theme-color': val,
    '--theme-light': adjustColor(val, 30),
    '--theme-dark': adjustColor(val, -30)
  }
  localStorage.setItem('rpc_theme', val)
}, { immediate: true })

const connected = ref(false)
const isLoading = ref(false)
const showGuideModal = ref(false)
const showChangelogModal = ref(false)
const minimizeToTray = ref(true)

const currentVersion = 'v1.3.0'
const changelog = [
  { version: 'v1.3.0', date: 'Marzo 2026', changes: ['Theming: Ahora puedes colorear e impregnar de tu tono favorito a toda la interfaz desde la paleta superior.', 'Integración total con iconos System-Tray: Ahora la aplicación puede minimizarse sin cerrarse por completo en PC.', 'Agregados hermosos spinners (indicadores de carga) al solicitar comandos de red.'] },
  { version: 'v1.2.0', date: 'Marzo 2026', changes: ['Incrustado Panel Interactivo de "Vista Previa en Vivo". Ahora ves los enlaces funcionando antes de guardar y enviarlos a tu perfil de Discord.'] }
]

const form = ref({ client_id: '' })
const toast = ref({ show: false, type: 'success', message: '' })

function showToast(type, msg) {
  toast.value = { show: true, type, message: msg }
  setTimeout(() => toast.value.show = false, 3000)
}

const rpc = ref({
  state: '', details: '', large_image: '', large_text: '', small_image: '', small_text: ''
})

const apiBase = 'http://127.0.0.1:8000/api'

async function connect() {
  isLoading.value = true
  try {
    const res = await fetch(`${apiBase}/connect`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ client_id: form.value.client_id })
    })
    if (res.ok) {
      connected.value = true
      showToast('success', '¡Conectado a tu cliente de Discord Exitosamente!')
    } else {
      const err = await res.json()
      showToast('error', 'Error: ' + err.detail)
    }
  } catch(e) {
    showToast('error', "Error de red al conectar al motor interno. ¿Se cerró el programa?")
  }
  isLoading.value = false
}

async function updateRPC() {
  isLoading.value = true
  try {
    const res = await fetch(`${apiBase}/update`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(rpc.value)
    })
    if (res.ok) {
      showToast('success', '¡Estado actualizado con éxito!')
    } else {
      const err = await res.json()
      showToast('error', 'Error al actualizar: ' + err.detail)
      connected.value = false
    }
  } catch(e) {
    showToast('error', "Error al intentar actualizar el RPC.")
  }
  isLoading.value = false
}

async function disconnect() {
  try {
    await fetch(`${apiBase}/disconnect`, { method: 'POST' })
  } finally {
    connected.value = false
  }
}

async function updateTraySetting() {
  try {
    await fetch(`${apiBase}/settings`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ minimize_to_tray: minimizeToTray.value })
    })
  } catch(e) { }
}

onMounted(async () => {
  try {
    const res = await fetch(`${apiBase}/status`)
    if(res.ok) {
      const data = await res.json()
      minimizeToTray.value = data.minimize_to_tray
      if (data.connected) {
        connected.value = true
        form.value.client_id = data.client_id
      }
    }
  } catch(e) {}
})
</script>

<style>
/* For checkbox overriding Tailwind form defaults if needed */
[type='checkbox']:checked {
  background-color: var(--theme-color);
  border-color: var(--theme-color);
}
.animate-fade-in { animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
@keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
.toast-enter-active, .toast-leave-active { transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
.toast-enter-from, .toast-leave-to { opacity: 0; transform: translate(-50%, -30px); }
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
