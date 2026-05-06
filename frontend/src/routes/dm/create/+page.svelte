<script>
  let name = "";
  let description = "";
  let map = null;
  let maxPlayers = 5;
  let ruleset = "dnd5e";
</script>

<div class="min-h-screen bg-[url('/parchment-dark.jpg')] text-yellow-100 font-serif p-6">

  <div class="max-w-5xl mx-auto border-4 border-yellow-600 bg-black/70 p-6">

    <h1 class="text-2xl text-yellow-400 mb-4 tracking-widest">
      🏰 Criar Nova Aventura
    </h1>

    <div class="grid grid-cols-3 gap-4">

      <!-- 📝 FORM -->
      <div class="col-span-1 space-y-3">

        <input
          bind:value={name}
          placeholder="Nome da campanha"
          class="w-full p-2 bg-black border border-yellow-600"
        />

        <textarea
          bind:value={description}
          placeholder="Descrição da aventura"
          class="w-full p-2 bg-black border border-yellow-600 h-32"
        />

        <input
          type="number"
          bind:value={maxPlayers}
          class="w-full p-2 bg-black border border-yellow-600"
          placeholder="Max players"
        />

        <select class="w-full p-2 bg-black border border-yellow-600">
          <option>D&D 5e</option>
          <option>Custom</option>
        </select>

        <button class="w-full p-2 bg-yellow-900/30 border border-yellow-600">
          Criar Sala
        </button>

      </div>

      <!-- 🗺️ MAPA -->
      <div class="col-span-1 border border-yellow-600 bg-black/40 flex items-center justify-center">
        <p class="opacity-60">Upload de mapa aqui</p>
      </div>

      <!-- ⚙️ CONFIG -->
      <div class="col-span-1 border border-yellow-600 p-3 bg-black/40 text-sm">

        <p class="text-yellow-400 mb-2">⚙️ Configurações</p>

        <label class="block mb-2">
          <input type="checkbox" /> Fog of War
        </label>

        <label class="block mb-2">
          <input type="checkbox" /> Roll público
        </label>

        <label class="block mb-2">
          <input type="checkbox" /> Turn order automática
        </label>

      </div>

    </div>
  </div>
</div>