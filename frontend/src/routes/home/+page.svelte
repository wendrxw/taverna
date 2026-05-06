<script>
  let menu = [
    "🏰 Início da Guilda",
    "⚔️ Campanhas",
    "🧙 Personagens",
    "📜 Regras da Mesa",
    "💰 Loot & Inventário",
    "🔥 Combate ao vivo"
  ];

  let pageTitle = "Crônicas de Taverna";
</script>

<!-- ✅ FIX: layout em coluna ocupando altura total -->
<div class="min-h-screen flex flex-col bg-[url('/parchment-dark.jpg')] bg-cover text-yellow-100 font-serif">

  <!-- 🏰 HEADER -->
  <header class="border-b-4 border-yellow-600 bg-black/70 shadow-lg">
    <div class="p-6 text-center">
      <h1 class="text-4xl tracking-[0.4em] text-yellow-400 drop-shadow-[0_0_10px_rgba(255,215,0,0.4)]">
        ⚔️ CRÔNICAS DA TAVERNA ⚔️
      </h1>
      <p class="text-sm opacity-70 uppercase tracking-widest">
        Portal da Guilda • RPG de Mesa Online
      </p>
    </div>
  </header>

  <!-- 📜 MAIN (OCUPA TODO ESPAÇO RESTANTE) -->
  <div class="flex flex-1 min-h-0">

    <!-- 🧭 SIDEBAR -->
    <aside class="w-72 bg-black/80 border-r-4 border-yellow-600 p-4">

      <h2 class="text-yellow-400 mb-4 tracking-widest">
        🏹 Menu da Guilda
      </h2>

      <ul class="space-y-2">
        {#each menu as item}
          <li class="p-2 border border-yellow-700 bg-black/50 hover:bg-yellow-900/20 cursor-pointer transition">
            {item}
          </li>
        {/each}
      </ul>

      <div class="mt-6 text-xs opacity-60">
        ⚔️ Status do servidor: ONLINE<br/>
        🧙 Mestres ativos: 2<br/>
        👥 Aventureiros: 14
      </div>

    </aside>

    <!-- 📖 CONTEÚDO -->
    <main class="flex-1 p-8 bg-black/60">

      <div class="border-2 border-yellow-600 p-6 bg-black/70 shadow-[inset_0_0_25px_rgba(255,215,0,0.1)]">

        <h2 class="text-2xl text-yellow-300 mb-4 tracking-widest">
          📜 Bem-vindo, Aventureiro
        </h2>

        <p class="opacity-80 leading-relaxed">
          Este é o portal oficial da campanha. Aqui você encontrará regras,
          personagens, sessões e o fluxo completo do combate em tempo real.
        </p>

        <div class="mt-6 grid grid-cols-2 gap-4">

          <div class="border border-yellow-700 p-3 bg-black/50">
            ⚔️ Campanhas ativas<br/>
            <span class="text-yellow-400">3 aventuras em andamento</span>
          </div>

          <div class="border border-yellow-700 p-3 bg-black/50">
            📜 Última sessão<br/>
            <span class="text-yellow-400">O Cemitério dos Magos</span>
          </div>

        </div>

      </div>

    </main>
  </div>

  <!-- 🧾 FOOTER (SEM ESPAÇO SOBRANDO) -->
  <footer class="border-t-4 border-yellow-600 bg-black/80 p-3 text-center text-xs opacity-70">
    ⚔️ Taverna RPG Engine • Medieval Fantasy System • v0.1
  </footer>

</div>