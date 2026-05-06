<script>
  let name = $state("Arthas");
  let classLevel = $state("Fighter 1");
  let background = $state("Noble");
  let race = $state("Human");
  let alignment = $state("Lawful Neutral");
  let xp = $state(0);

  let str = $state(16);
  let dex = $state(9);
  let con = $state(15);
  let int = $state(11);
  let wis = $state(13);
  let cha = $state(14);

  let ac = $state(17);
  let initiative = $state(-1);
  let speed = $state(30);

  let hpMax = $state(12);
  let hpCurrent = $state(12);
  let hpTemp = $state(0);
  
  import { generateByClass } from "$lib/characterEngine";

  function randomCharacter() {
    const classes = ["Fighter", "Wizard", "Rogue"];
    const chosen = classes[Math.floor(Math.random() * classes.length)];

    const stats = generateByClass(chosen);

    str = stats.str;
    dex = stats.dex;
    con = stats.con;
    int = stats.int;
    wis = stats.wis;
    cha = stats.cha;

    classLevel = `${chosen} 1`;
  }
</script>

<div class="min-h-screen bg-[url('/parchment-dark.jpg')] text-yellow-100 font-serif p-4">

  <!-- 🧾 SHEET CONTAINER -->
  <div class="max-w-6xl mx-auto border-4 border-yellow-600 bg-black/70 p-4 shadow-2xl">
    <!-- ⚔️ ACTION BAR -->
    <div class="flex justify-between items-center mb-3 border-2 border-yellow-700 bg-black/60 p-2">

    <div class="text-yellow-400 text-sm tracking-widest">
        ⚔️ Character Sheet
    </div>

    <div class="flex gap-2">

        <button
        on:click={saveCharacter}
        class="px-3 py-1 border border-yellow-600 bg-black hover:bg-yellow-900/30 text-yellow-200 text-sm"
        >
        💾 Save
        </button>

        <button
        on:click={resetCharacter}
        class="px-3 py-1 border border-yellow-600 bg-black hover:bg-yellow-900/30 text-yellow-200 text-sm"
        >
        🔄 Reset
        </button>

        <button
        on:click={randomCharacter}
        class="px-3 py-1 border border-yellow-600 bg-black hover:bg-yellow-900/30 text-yellow-200 text-sm"
        >
        🎲 Random
        </button>

    </div>

    </div>
    <!-- 🏷️ HEADER -->
    <div class="grid grid-cols-12 gap-2 border-b-2 border-yellow-700 pb-2 mb-3 text-xs">

      <div class="col-span-4 border border-yellow-700 p-2 bg-black/40">
        <div class="uppercase text-[10px] text-yellow-400">Character Name</div>
        <input bind:value={name}
          class="w-full font-bold outline-none bg-transparent text-yellow-100" />
      </div>

      <div class="col-span-2 border border-yellow-700 p-2 bg-black/40">
        <div class="uppercase text-[10px] text-yellow-400">Class & Level</div>
        <input bind:value={classLevel}
          class="w-full outline-none bg-transparent text-yellow-100" />
      </div>

      <div class="col-span-2 border border-yellow-700 p-2 bg-black/40">
        <div class="uppercase text-[10px] text-yellow-400">Background</div>
        <input bind:value={background}
          class="w-full outline-none bg-transparent text-yellow-100" />
      </div>

      <div class="col-span-2 border border-yellow-700 p-2 bg-black/40">
        <div class="uppercase text-[10px] text-yellow-400">Player Name</div>
        <input class="w-full outline-none bg-transparent text-yellow-100" />
      </div>

      <div class="col-span-2 border border-yellow-700 p-2 bg-black/40">
        <div class="uppercase text-[10px] text-yellow-400">Race</div>
        <input bind:value={race}
          class="w-full outline-none bg-transparent text-yellow-100" />
      </div>

    </div>

    <!-- 🧱 MAIN GRID -->
    <div class="grid grid-cols-12 gap-2">

      <!-- 🧍 LEFT STATS -->
      <div class="col-span-3 space-y-2">

        {#each [
          ["STR", str],
          ["DEX", dex],
          ["CON", con],
          ["INT", int],
          ["WIS", wis],
          ["CHA", cha]
        ] as stat}

          <div class="border border-yellow-700 p-2 text-center bg-black/40">
            <div class="text-xs text-yellow-400">{stat[0]}</div>
            <div class="text-2xl font-bold text-yellow-100">{stat[1]}</div>
          </div>

        {/each}

      </div>

      <!-- 🧠 CENTER COMBAT -->
      <div class="col-span-6 space-y-2">

        <div class="grid grid-cols-3 gap-2">

          <div class="border border-yellow-700 p-2 text-center bg-black/40">
            <div class="text-xs text-yellow-400">AC</div>
            <div class="text-xl font-bold">{ac}</div>
          </div>

          <div class="border border-yellow-700 p-2 text-center bg-black/40">
            <div class="text-xs text-yellow-400">INIT</div>
            <div class="text-xl font-bold">{initiative}</div>
          </div>

          <div class="border border-yellow-700 p-2 text-center bg-black/40">
            <div class="text-xs text-yellow-400">SPEED</div>
            <div class="text-xl font-bold">{speed}</div>
          </div>

        </div>

        <!-- HP -->
        <div class="border border-yellow-700 p-2 bg-black/40">
          <div class="text-xs uppercase text-yellow-400">Hit Points</div>

          <div class="flex gap-2 mt-2">
            <input bind:value={hpCurrent}
              class="w-1/3 border border-yellow-700 p-1 text-center bg-black text-yellow-100" />
            <input bind:value={hpMax}
              class="w-1/3 border border-yellow-700 p-1 text-center bg-black text-yellow-100" />
            <input bind:value={hpTemp}
              class="w-1/3 border border-yellow-700 p-1 text-center bg-black text-yellow-100" />
          </div>
        </div>

        <div class="border border-yellow-700 p-2 h-40 bg-black/40">
          <div class="text-xs uppercase text-yellow-400 mb-2">Attacks & Spellcasting</div>
        </div>

        <div class="border border-yellow-700 p-2 h-40 bg-black/40">
          <div class="text-xs uppercase text-yellow-400 mb-2">Features & Traits</div>
        </div>

      </div>

      <!-- 📜 RIGHT SIDE -->
      <div class="col-span-3 space-y-2">

        {#each ["Personality", "Ideals", "Bonds", "Flaws"] as box}

          <div class="border border-yellow-700 p-2 h-32 bg-black/40">
            <div class="text-xs uppercase text-yellow-400">{box}</div>
          </div>

        {/each}

      </div>

    </div>
  </div>
</div>