#!/bin/bash
for f in "$@"; do [ -f "$f" ] && chmod +x "$f"; done
