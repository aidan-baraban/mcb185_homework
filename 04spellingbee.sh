gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E "r" | grep -E "^[zoniacr]{4,}$" | grep -v -E "[^zoniacr]"
