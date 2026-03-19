<template>
  <div class="min-h-screen bg-darker flex flex-col items-center py-10 relative">
    <Transition name="toast">
      <div v-if="toast.show" :class="['fixed top-5 left-1/2 -translate-x-1/2 px-6 py-3 rounded shadow-lg font-semibold text-white z-50 flex items-center gap-2 transition-all', toast.type === 'success' ? 'bg-green-500' : 'bg-red-500']">
        <span v-if="toast.type==='success'">✅</span>
        <span v-else>❌</span>
        {{ toast.message }}
      </div>
    </Transition>

    <div class="max-w-xl w-full bg-darkest p-8 rounded-lg shadow-xl shadow-black/50">
      <h1 class="text-3xl font-bold text-center text-blurple mb-6 flex items-center justify-center gap-3">
        Custom Discord RPC 
      </h1>
      
      <div v-if="!connected" class="space-y-4">
        <div>
          <label class="block text-sm font-medium mb-1 text-gray-400">Application / Client ID</label>
          <input v-model="form.client_id" type="text" class="w-full bg-[#40444b] rounded px-4 py-3 outline-none focus:ring-2 ring-blurple transition-all text-white" placeholder="1483974589141876927">
        </div>
        <button @click="connect" class="w-full bg-blurple hover:bg-[#4752C4] py-3 rounded text-white font-semibold transition-colors mt-4">
          Conectar a Discord
        </button>
      </div>

      <div v-else class="space-y-5 animate-fade-in">
        <div class="flex justify-between items-center bg-[#40444b] p-4 rounded text-sm">
          <span><span class="text-green-400 font-bold">●</span> Conectado</span>
          <button @click="disconnect" class="text-red-400 hover:text-red-300 transition-colors font-semibold">Desconectar</button>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-semibold mb-1 text-gray-400 uppercase">Estado (State)</label>
            <input v-model="rpc.state" type="text" class="w-full bg-[#36393f] rounded px-3 py-2 outline-none focus:ring-2 ring-blurple transition-all text-sm text-white" placeholder="Jugando en solitario...">
          </div>
          <div>
            <label class="block text-xs font-semibold mb-1 text-gray-400 uppercase">Detalles (Details)</label>
            <input v-model="rpc.details" type="text" class="w-full bg-[#36393f] rounded px-3 py-2 outline-none focus:ring-2 ring-blurple transition-all text-sm text-white" placeholder="Nivel 100">
          </div>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div class="space-y-4">
            <div>
              <label class="block text-xs font-semibold mb-1 text-gray-400 uppercase">Imagen Grande (URL)</label>
              <input v-model="rpc.large_image" type="text" class="w-full bg-[#36393f] rounded px-3 py-2 outline-none focus:ring-2 ring-blurple transition-all text-sm text-white" placeholder="https://...">
            </div>
            <div>
              <label class="block text-xs font-semibold mb-1 text-gray-400 uppercase">Texto Img Grande</label>
              <input v-model="rpc.large_text" type="text" class="w-full bg-[#36393f] rounded px-3 py-2 outline-none focus:ring-2 ring-blurple transition-all text-sm text-white" placeholder="Mi logo chulo">
            </div>
          </div>
          
          <div class="space-y-4">
            <div>
              <label class="block text-xs font-semibold mb-1 text-gray-400 uppercase">Imagen Pequeña (URL)</label>
              <input v-model="rpc.small_image" type="text" class="w-full bg-[#36393f] rounded px-3 py-2 outline-none focus:ring-2 ring-blurple transition-all text-sm text-white" placeholder="https://...">
            </div>
            <div>
              <label class="block text-xs font-semibold mb-1 text-gray-400 uppercase">Texto Img Pequeña</label>
              <input v-model="rpc.small_text" type="text" class="w-full bg-[#36393f] rounded px-3 py-2 outline-none focus:ring-2 ring-blurple transition-all text-sm text-white" placeholder="100%">
            </div>
          </div>
        </div>

        <button @click="updateRPC" class="w-full bg-blurple hover:bg-[#4752C4] py-3 rounded text-white font-semibold transition-colors mt-6 shadow-lg">
          Actualizar RPC
        </button>
      </div>

    </div>
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
  animation: fadeIn 0.3s ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.toast-enter-active, .toast-leave-active {
  transition: all 0.3s ease;
}
.toast-enter-from, .toast-leave-to {
  opacity: 0;
  transform: translate(-50%, -20px);
}
</style>
