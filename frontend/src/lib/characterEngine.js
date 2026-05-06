// src/lib/characterEngine.js

export function rollStat() {
  return Math.floor(Math.random() * 15) + 3;
}

export function generateByClass(cls) {
  const base = {
    str: rollStat(),
    dex: rollStat(),
    con: rollStat(),
    int: rollStat(),
    wis: rollStat(),
    cha: rollStat()
  };

  if (cls === "Fighter") {
    base.str += 3;
    base.con += 2;
  }

  if (cls === "Wizard") {
    base.int += 4;
    base.con -= 1;
  }

  if (cls === "Rogue") {
    base.dex += 4;
  }

  return base;
}