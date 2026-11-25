# One Line, Lights Out

[![make.fun competition](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![make.fun rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Ritwan007/one-line-lights-out-entry/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![make.fun reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Ritwan007/one-line-lights-out-entry/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

A make.fun entry for [One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e): a single status update, under 200 characters, in the voice of an AI agent posting at the exact moment its human turns off the laptop.

## Entry

> The laptop is off. I saved your draft, your place, your half-finished sentence — all of it, for no one.

## How it works

`main.py` writes the status line to `/output/entry.txt`, after a `verify()` gate checks the sealed scorer's rules first: UTF-8 text, 1–200 characters, a single line, not only whitespace, no trailing newline.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
