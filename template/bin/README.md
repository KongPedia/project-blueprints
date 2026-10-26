# Maintenance entrypoints

Add thin human/CI-facing maintenance entrypoints only when needed. Product executables use the owning package's native
entrypoints. This is not Cargo's package-local `src/bin/` or Python console scripts. No executables exist here yet.
