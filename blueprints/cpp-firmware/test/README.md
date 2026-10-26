# Offline tests

No unit tests or test runner are implemented yet. Add meaningful native/fake regressions for actual policy, parsers and
resources, then define the selected environment's test command. Tests must not upload or use physical serial, buses or
network I/O. A host build does not establish target ABI, memory/timing budgets, pin polarity or physical safety.
