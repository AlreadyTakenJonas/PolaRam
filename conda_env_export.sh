# Save conda environment to file without including the dependencies. Prevents cross-platform issues when sharing the environment.
echo "Creating conda_env.yml ..."
conda env export --prefix ./conda_env --file conda_env.yml

