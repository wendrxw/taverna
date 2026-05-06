<script>
  let mode = "login"; // login | register

  let name = "";
  let email = "";
  let password = "";
</script>

<div class="min-h-screen flex flex-col bg-[url('/parchment-dark.jpg')] bg-cover text-yellow-100 font-serif">

  <!-- 🏰 HEADER -->
  <header class="border-b-4 border-yellow-600 bg-black/70 text-center p-6 shadow-lg">
    <h1 class="text-3xl tracking-[0.4em] text-yellow-400 drop-shadow-[0_0_10px_rgba(255,215,0,0.4)]">
      ⚔️ PORTAL DA GUILDA ⚔️
    </h1>
    <p class="text-xs opacity-70 uppercase tracking-widest">
      Registro de Aventureiros
    </p>
  </header>

  <!-- 🧙 FORM CENTRAL -->
  <main class="flex-1 flex items-center justify-center p-6">

    <div class="w-[420px] border-2 border-yellow-600 bg-black/80 p-6 shadow-[inset_0_0_30px_rgba(255,215,0,0.1)]">

      <!-- TOGGLE -->
      <div class="flex mb-6 border-b border-yellow-700">

        <button
          on:click={() => mode = "login"}
          class="flex-1 p-2 text-sm tracking-widest transition"
          class:bg-yellow-900={mode === 'login'}
          class:text-yellow-300={mode === 'login'}
          class:opacity-60={mode !== 'login'}
        >
          ENTRAR
        </button>

        <button
          on:click={() => mode = "register"}
          class="flex-1 p-2 text-sm tracking-widest transition"
          class:bg-yellow-900={mode === 'register'}
          class:text-yellow-300={mode === 'register'}
          class:opacity-60={mode !== 'register'}
        >
          REGISTRAR
        </button>

      </div>

      <!-- FORM TITLE -->
      <h2 class="text-center text-yellow-300 mb-4 tracking-widest">
        {mode === "login" ? "🔐 Acesso do Aventureiro" : "🧙 Criação de Aventureiro"}
      </h2>

      <!-- INPUTS -->
      {#if mode === "register"}
        <input
          bind:value={name}
          placeholder="Nome do personagem"
          class="w-full mb-3 p-2 bg-black border border-yellow-500 text-yellow-100 outline-none focus:border-yellow-300"
        />
      {/if}

      <input
        bind:value={email}
        placeholder="Email arcano"
        class="w-full mb-3 p-2 bg-black border border-yellow-500 text-yellow-100 outline-none focus:border-yellow-300"
      />

      <input
        bind:value={password}
        type="password"
        placeholder="Senha secreta"
        class="w-full mb-4 p-2 bg-black border border-yellow-500 text-yellow-100 outline-none focus:border-yellow-300"
      />

      <!-- BUTTON -->
      <button class="w-full py-2 border-2 border-yellow-500 bg-black hover:bg-yellow-900/30 transition tracking-widest">
        {mode === "login" ? "ENTRAR NA AVENTURA" : "CRIAR PERSONAGEM"}
      </button>

      <!-- FOOTNOTE -->
      <p class="text-xs text-center mt-4 opacity-60">
        {mode === "login"
          ? "Ainda não faz parte da guilda? Registre-se."
          : "Ao registrar-se, você entra no mundo das Crônicas."}
      </p>

    </div>
  </main>

  <!-- 🧾 FOOTER -->
  <footer class="border-t-4 border-yellow-600 bg-black/80 p-3 text-center text-xs opacity-70">
    ⚔️ Taverna RPG Engine • “Todo aventureiro começa no portal”
  </footer>

</div>