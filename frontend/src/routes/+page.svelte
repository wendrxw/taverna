<script>
  let features = [
    "⚔️ Combate em tempo real",
    "🎲 Sistema de dados integrado",
    "🧙 Personagens persistentes",
    "📜 Campanhas narradas pelo mestre",
  ];
</script>

<div class="min-h-screen bg-[url('/parchment-dark.jpg')] bg-cover text-yellow-100 font-serif flex flex-col">

  <!-- 🏰 HERO BANNER -->
  <header class="text-center py-16 border-b-4 border-yellow-600 bg-black/70 shadow-xl">

    <h1 class="text-5xl tracking-[0.4em] text-yellow-400 drop-shadow-[0_0_12px_rgba(255,215,0,0.5)]">
      ⚔️ TAVERNA RPG ⚔️
    </h1>

    <p class="mt-4 text-sm uppercase tracking-widest opacity-80">
      O portal das grandes campanhas de fantasia medieval
    </p>

    <button class="mt-6 px-6 py-2 border-2 border-yellow-500 bg-black/60 hover:bg-yellow-900/30 transition shadow-lg">
      Entrar na Aventura
    </button>

  </header>

  <!-- 📜 CONTEÚDO PRINCIPAL -->
  <main class="flex-1 p-10">

    <div class="grid grid-cols-3 gap-6">

      <!-- 📖 SOBRE -->
      <section class="border-2 border-yellow-600 bg-black/70 p-6 shadow-inner">

        <h2 class="text-xl text-yellow-300 mb-3 tracking-widest">
          📜 O que é o Taverna RPG?
        </h2>

        <p class="text-sm opacity-80 leading-relaxed">
          Um sistema de RPG de mesa online inspirado em Foundry e Roll20,
          com combate em tempo real, narrativa viva e suporte a campanhas épicas.
        </p>

        <ul class="mt-4 space-y-2 text-sm">
          {#each features as f}
            <li>• {f}</li>
          {/each}
        </ul>

      </section>

      <!-- 📺 CANAIS ONLINE -->
        <section class="border-2 border-yellow-600 bg-black/70 p-6 shadow-inner">

        <h2 class="text-xl text-yellow-300 mb-3 tracking-widest">
            📺 Canais Online
        </h2>

        <p class="text-xs opacity-60 mb-3">
            Aventureiros transmitindo suas campanhas ao vivo
        </p>

        <div class="space-y-3 text-sm">

            <div class="border border-green-600 p-3 bg-black/50 hover:bg-green-900/10 transition">
            🧙 ArcaneMageTV<br/>
            <span class="text-green-400 text-xs">🔴 AO VIVO • Masmorra de Eldoria</span>
            </div>

            <div class="border border-red-600 p-3 bg-black/50 hover:bg-red-900/10 transition">
            ⚔️ KnightSaga<br/>
            <span class="text-red-400 text-xs">🔴 AO VIVO • Guerra das Cinzas</span>
            </div>

            <div class="border border-blue-600 p-3 bg-black/50 hover:bg-blue-900/10 transition">
            🎲 Dice&Dragons<br/>
            <span class="text-blue-400 text-xs">🟡 EM BREVE • Sessão 12</span>
            </div>

        </div>

        </section>

      <!-- 🔐 LOGIN -->
      <section class="border-2 border-yellow-600 bg-black/70 p-6 shadow-inner">

        <h2 class="text-xl text-yellow-300 mb-3 tracking-widest">
          🔐 Entrar na Guilda
        </h2>

        <input
          placeholder="Nome do aventureiro"
          class="w-full mb-3 p-2 bg-black border border-yellow-500 text-yellow-100"
        />

        <input
          placeholder="Senha arcana"
          type="password"
          class="w-full mb-3 p-2 bg-black border border-yellow-500 text-yellow-100"
        />

        <button class="w-full py-2 border-2 border-yellow-500 bg-black hover:bg-yellow-900/30 transition">
          Entrar
        </button>

        <p class="text-xs mt-3 opacity-60">
          Novo aventureiro? Crie sua ficha.
        </p>

      </section>

    </div>
  </main>

  <!-- 🧾 FOOTER LORE -->
  <footer class="border-t-4 border-yellow-600 bg-black/80 p-4 text-center text-xs opacity-70">
    ⚔️ Taverna RPG Engine • Medieval Fantasy System • “Toda aventura começa em uma taverna”
  </footer>

</div>