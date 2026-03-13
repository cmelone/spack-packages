Creating a Spack package starts with understanding the target repository. The first step is to develop an understanding of how it builds:
- build system
- dependencies (languages, compilers, etc).
- build options
- conflicts
- other installation constraints

This means analyzing the build configuration and repository structure with these details in mind.

With this information in hand, the rest of the work becomes translation. Each meaningful build declaration found in the repository needs to map to Spack concepts: variants, dependencies, conflicts, etc. Not everything in the build files must be included; the final recipe should reflect what is useful to downstream consumers of the Spack package.

Once the recipe is created, validation is crucial. Spack tooling can help expose issues at several levels, from recipe syntax to installation, and each piece of feedback is an indication to revise the recipe. The process is complete when the package installs successfully. Keep in mind that Spack packages are combinatorial in nature, it is effectively impossible to test every combination of constraints; you should be judicious about you test based on the user's input.

If a failure traces back to a dependency rather than the package itself, that's a seperate problem and should be treated accordingly.

This repository may contain skills to assist during the process of recipe writing. Depending on the state of the recipe, they should be used in line with the general flow described in this document.

For more advanced guidelines, you should consult the Spack packaging guide:
- https://spack.readthedocs.io/en/latest/packaging_guide_creation.html
- https://spack.readthedocs.io/en/latest/packaging_guide_build.html
- https://spack.readthedocs.io/en/latest/packaging_guide_testing.html
- https://spack.readthedocs.io/en/latest/packaging_guide_advanced.html

## Invoking Spack in this environment

Plain `spack` resolves to a shell function that is not available in this shell. Always invoke spack via `$SPACK_ROOT/bin/spack`.

For spack commands scoped to an environment, prefer the `-e` flag — it works across shell invocations without needing activation:

  $SPACK_ROOT/bin/spack -e <env_name> find
  $SPACK_ROOT/bin/spack -e <env_name> install <spec>

To create a new managed environment:

  $SPACK_ROOT/bin/spack env create <env_name>
