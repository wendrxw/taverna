<script>
  let logs = [
    "⚔️ O grupo entra na masmorra sombria...",
    "🎲 Goblin rola iniciativa 17",
    "🔥 Mago conjura Firebolt!"
  ];

  let players = [
    { name: "Arthas", hp: 24, ac: 16, turn: true },
    { name: "Lyra", hp: 18, ac: 14, turn: false },
    { name: "Goblin", hp: 7, ac: 12, turn: false }
  ];

  let chat = [
    { user: "GM", msg: "Iniciem o combate." },
    { user: "Arthas", msg: "Ataco o goblin!" },
    { user: "Sistema", msg: "Arthas causa 6 de dano." }
  ];

  let input = "";
</script>

<div class="h-screen flex flex-col bg-[url('/parchment-dark.jpg')] bg-cover text-yellow-100 font-serif">

  <!-- 🏰 TOP BAR -->
  <header class="border-b-4 border-yellow-600 bg-black/80 p-3 flex justify-between items-center">
    <div>
      <h1 class="text-xl tracking-widest text-yellow-400">⚔️ Mesa de Aventura</h1>
      <p class="text-xs opacity-60">Sessão ativa • Dungeon Crawl</p>
    </div>

    <div class="text-xs opacity-70">
      🔥 Combate: ATIVO • 🎲 Round 2 • ⏳ Turno: Arthas
    </div>
  </header>

  <!-- 🎯 MAIN -->
  <div class="flex flex-1 overflow-hidden">

    <!-- 🧭 MENU AÇÕES (MENOR) -->
    <aside class="w-48 border-r-4 border-yellow-600 bg-black/70 p-2">
      <h2 class="text-yellow-400 text-sm mb-2 tracking-widest">⚔️ Ações</h2>

      <div class="space-y-2 text-xs">

        <button class="w-full p-2 border border-yellow-700 bg-black/40 hover:bg-yellow-900/20">
          Atacar
        </button>

        <button class="w-full p-2 border border-yellow-700 bg-black/40 hover:bg-yellow-900/20">
          Magia
        </button>

        <button class="w-full p-2 border border-yellow-700 bg-black/40 hover:bg-yellow-900/20">
          Defender
        </button>

        <button class="w-full p-2 border border-yellow-700 bg-black/40 hover:bg-yellow-900/20">
          Inventário
        </button>

      </div>
    </aside>

    <!-- 🗺️ MAPA (MAIOR AREA CENTRAL) -->
    <main class="flex-1 p-3 flex items-center justify-center">
      <div class="relative w-full h-full border-4 border-yellow-600 bg-black/60">

        <!-- GRID -->
        <div class="grid grid-cols-12 grid-rows-12 w-full h-full opacity-25">
          {#each Array(144) as _}
            <div class="border border-yellow-900/30"></div>
          {/each}
        </div>

        <!-- TOKENS -->
        <div class="absolute top-[25%] left-[30%]">
          <div class="w-8 h-8 bg-blue-500 border border-white rounded-full flex items-center justify-center text-xs">
            A
          </div>
        </div>

        <div class="absolute top-[50%] left-[55%]">
          <div class="w-8 h-8 bg-red-500 border border-white rounded-full flex items-center justify-center text-xs">
            G
          </div>
        </div>

      </div>
    </main>

    <!-- 💬 CHAT (MAIOR QUE MENU) -->
    <aside class="w-[420px] border-l-4 border-yellow-600 bg-black/80 flex flex-col">

      <div class="p-2 border-b border-yellow-700">
        <h2 class="text-yellow-400 text-sm tracking-widest">💬 Crônicas & Ações</h2>
      </div>

      <!-- MENSAGENS -->
      <div class="flex-1 overflow-auto p-2 space-y-2 text-xs">
        {#each chat as c}
          <div class="border border-white/10 p-2 bg-black/40">
            <span class="text-yellow-400">{c.user}:</span>
            <span class="opacity-80">{c.msg}</span>
          </div>
        {/each}
      </div>

      <!-- INPUT -->
      <div class="p-2 border-t border-yellow-700">
        <input
          bind:value={input}
          placeholder="Digite ação ou mensagem..."
          class="w-full p-2 bg-black border border-yellow-500 text-yellow-100 text-xs"
        />
      </div>

    </aside>

  </div>
</div>