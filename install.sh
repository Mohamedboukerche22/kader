#!/bin/bash

set -e

SCRIPT="kader.py"
INSTALL_DIR="$HOME/.local/bin"

mkdir -p "$INSTALL_DIR"

# Add shebang if missing
if ! head -n1 "$SCRIPT" | grep -q "^#!/usr/bin/env python3"; then
    sed -i '1i#!/usr/bin/env python3' "$SCRIPT"
fi

chmod +x "$SCRIPT"

cp "$SCRIPT" "$INSTALL_DIR/kader"

echo "Installed to $INSTALL_DIR/kader"

# Add ~/.local/bin to PATH if needed
if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
    echo "Added ~/.local/bin to PATH."
    echo "Run: source ~/.bashrc"
fi

echo "You can now run:"
echo "    kader"