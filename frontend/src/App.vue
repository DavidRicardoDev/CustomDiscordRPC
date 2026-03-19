<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-[#1a1c23] to-[#121318] flex flex-col items-center justify-center py-10 relative px-4 font-sans text-gray-100">
    <Transition name="toast">
      <div v-if="toast.show" :class="['fixed top-6 left-1/2 -translate-x-1/2 px-6 py-3 rounded-xl shadow-2xl font-semibold text-white z-50 flex items-center gap-3 backdrop-blur-md', toast.type === 'success' ? 'bg-emerald-500/90 border border-emerald-400/50' : 'bg-rose-500/90 border border-rose-400/50']">
        <span v-if="toast.type==='success'" class="text-xl">✨</span>
        <span v-else class="text-xl">⚠️</span>
        {{ toast.message }}
      </div>
    </Transition>

    <div class="max-w-2xl w-full bg-[#2b2d31]/80 backdrop-blur-xl border border-white/10 p-8 sm:p-10 rounded-3xl shadow-2xl relative overflow-hidden mt-4">
      <!-- Decoración de fondo -->
      <div class="absolute top-0 right-0 -mr-20 -mt-20 w-64 h-64 rounded-full bg-indigo-500/20 blur-3xl pointer-events-none"></div>
      <div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-64 h-64 rounded-full bg-blue-500/10 blur-3xl pointer-events-none"></div>

      <div class="relative z-10">
        <h1 class="text-3xl sm:text-4xl font-extrabold text-center mb-8 tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-blue-400 to-blue-200">
          Presencia de discord personalizada
        </h1>
        
        <div v-if="!connected" class="space-y-6 max-w-sm mx-auto mt-4">
          <div class="space-y-2">
            <label class="block text-sm font-semibold text-gray-300 ml-1">Client ID (Application ID)</label>
            <input v-model="form.client_id" type="text" class="w-full bg-[#1e1f22] border border-white/5 rounded-xl px-4 py-3.5 outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all text-white placeholder-gray-500 shadow-inner" placeholder="Ej: 1483974589141876927">
          </div>
          <button @click="connect" class="w-full bg-indigo-500 hover:bg-indigo-400 active:bg-indigo-600 py-3.5 rounded-xl text-white font-bold transition-all transform hover:-translate-y-0.5 shadow-lg hover:shadow-indigo-500/25">
            Conectar Perfil
          </button>
        </div>

        <div v-else class="space-y-8 animate-fade-in mt-4">
          
          <div class="flex flex-col sm:flex-row justify-between items-center bg-[#1e1f22]/80 border border-white/5 p-4 rounded-2xl gap-4">
            <div class="flex items-center gap-3">
              <span class="relative flex h-3 w-3">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
              </span>
              <span class="font-medium text-emerald-400">Enlazado a Discord</span>
            </div>
            <button @click="disconnect" class="text-rose-400 hover:text-rose-300 text-sm font-semibold transition-colors bg-rose-500/10 hover:bg-rose-500/20 px-4 py-2 rounded-lg">
              Desconectar
            </button>
          </div>

          <div class="space-y-6">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
              <div class="space-y-1.5">
                <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Estado (State)</label>
                <input v-model="rpc.state" type="text" class="w-full bg-[#1e1f22] border border-white/5 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-indigo-500 transition-all text-sm text-gray-100 placeholder-gray-600 shadow-inner" placeholder="Ej: Explorando mazmorras...">
              </div>
              <div class="space-y-1.5">
                <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Detalles (Details)</label>
                <input v-model="rpc.details" type="text" class="w-full bg-[#1e1f22] border border-white/5 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-indigo-500 transition-all text-sm text-gray-100 placeholder-gray-600 shadow-inner" placeholder="Ej: Nivel 100">
              </div>
            </div>

            <div class="bg-[#1e1f22]/50 p-5 rounded-2xl border border-white/5 space-y-4">
              <h3 class="text-sm font-bold text-gray-300 border-b border-gray-700/50 pb-2">🖼️ Imagen Principal (Grande)</h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                <div class="space-y-1.5">
                  <label class="block text-xs font-semibold text-gray-400 ml-1">Enlace a Imagen (URL)</label>
                  <input v-model="rpc.large_image" type="text" class="w-full bg-[#2b2d31] rounded-lg px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-blue-500 transition-all text-sm text-gray-200 placeholder-gray-600 border border-transparent focus:border-blue-500/50" placeholder="https://imgur.com/foto.png">
                </div>
                <div class="space-y-1.5">
                  <label class="block text-xs font-semibold text-gray-400 ml-1">Texto al pasar el mouse</label>
                  <input v-model="rpc.large_text" type="text" class="w-full bg-[#2b2d31] rounded-lg px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-blue-500 transition-all text-sm text-gray-200 placeholder-gray-600 border border-transparent focus:border-blue-500/50" placeholder="Logo de mi servidor">
                </div>
              </div>
            </div>

            <div class="bg-[#1e1f22]/50 p-5 rounded-2xl border border-white/5 space-y-4">
              <h3 class="text-sm font-bold text-gray-300 border-b border-gray-700/50 pb-2">⭐ Imagen Secundaria (Pequeña)</h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                <div class="space-y-1.5">
                  <label class="block text-xs font-semibold text-gray-400 ml-1">Enlace a Imagen (URL)</label>
                  <input v-model="rpc.small_image" type="text" class="w-full bg-[#2b2d31] rounded-lg px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-blue-500 transition-all text-sm text-gray-200 placeholder-gray-600 border border-transparent focus:border-blue-500/50" placeholder="https://imgur.com/icono.gif">
                </div>
                <div class="space-y-1.5">
                  <label class="block text-xs font-semibold text-gray-400 ml-1">Texto al pasar el mouse</label>
                  <input v-model="rpc.small_text" type="text" class="w-full bg-[#2b2d31] rounded-lg px-3.5 py-2.5 outline-none focus:ring-2 focus:ring-blue-500 transition-all text-sm text-gray-200 placeholder-gray-600 border border-transparent focus:border-blue-500/50" placeholder="Rango Administrador">
                </div>
              </div>
            </div>
          </div>

          <button @click="updateRPC" class="w-full bg-gradient-to-r from-indigo-500 to-blue-600 hover:from-indigo-400 hover:to-blue-500 active:from-indigo-600 active:to-blue-700 py-4 rounded-xl text-white font-extrabold text-lg transition-all transform hover:-translate-y-0.5 shadow-xl hover:shadow-indigo-500/25 mt-2">
            🚀 Actualizar Presencia en Discord
          </button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="mt-8 mb-2 text-center z-10">
      <p class="text-gray-500 text-sm font-medium tracking-wide">
        Creado por <span class="text-indigo-400 font-bold">ShyLuns</span> (David Peña)
      </p>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const connected = ref(false)
const form = ref({
  client_id: '1483974589141876927'
})

const toast = ref({ show: false, type: 'success', message: '' })

function showToast(type, msg) {
  toast.value = { show: true, type, message: msg }
  setTimeout(() => toast.value.show = false, 3000)
}

const rpc = ref({
  state: '',
  details: '',
  large_image: '',
  large_text: '',
  small_image: '',
  small_text: ''
})

const apiBase = 'http://127.0.0.1:8000/api'

async function connect() {
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
}

async function updateRPC() {
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
}

async function disconnect() {
  try {
    await fetch(`${apiBase}/disconnect`, { method: 'POST' })
  } finally {
    connected.value = false
  }
}

onMounted(async () => {
  try {
    const res = await fetch(`${apiBase}/status`)
    if(res.ok) {
      const data = await res.json()
      if (data.connected) {
        connected.value = true
        form.value.client_id = data.client_id
      }
    }
  } catch(e) {
    // Normal al abrir porque fastapi y vite arrancan en orden aleatorio
  }
})
</script>

<style>
.animate-fade-in {
  animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}

.toast-enter-active, .toast-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.toast-enter-from, .toast-leave-to {
  opacity: 0;
  transform: translate(-50%, -30px);
}
</style>
