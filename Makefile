.PHONY: demo clean

demo:
	python examples/demo_sbo_luhs.py

clean:
	rm -rf logs/*.jsonl logs/*.log || true
