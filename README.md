# swift-py-doc

This site is to host the documentation for the `swift2` python package, which is part of a suite of tools for [Streamflow Forecasting](https://csiro-hydroinformatics.github.io/streamflow-forecasting-tools-onboard/).

## Updating the content of site

_These are notes to "self"_

### Copy doc files from reference repo

```bash
pkg_dir=${HOME}/src/swift/bindings/python/swift2
doc_dir=${HOME}/src/swift-py-doc
declare -a fn=(calibrate_multisite.ipynb \
  calibrate_subcatchments.ipynb \
  calibration_initial_states.ipynb \
  ensemble_model_runs.ipynb \
  error_correction_four_stages.ipynb \
  getting_started.ipynb \
  log_likelihood.ipynb \
  meta_parameters.ipynb \
  muskingum_multilink_calibration.ipynb \
  reservoir_geometry.ipynb)

cd ${doc_dir}
# WARNING: rm -r...
rm -r docs
cp ${pkg_dir}/mkdocs.yml ${doc_dir}/
cp -r ${pkg_dir}/docs ${doc_dir}/
cp ${pkg_dir}/LICENSE.txt ${doc_dir}/docs/license.md


# Iterate through the array 'fn'
for f in "${fn[@]}"; do
  file=${pkg_dir}/notebooks/${f}
  # Check if the file exists
  if [[ ! -f "$file" ]]; then
    echo "File '$file' does NOT exist."
  fi
done
# muskingum_multilink_calibration_explanation.ipynb

mkdir -p ${doc_dir}/docs/notebooks
cd ${doc_dir}/docs/notebooks
rm *.ipynb
cp ${pkg_dir}/notebooks/*.png ./
```

### Execute notebooks in-place

This may take a few minutes to run, esp. if run from debug build.

```sh
# kernel_name=hydrofc_release
kernel_name=hydrofc

for f in ${fn[@]} ; do
    echo "processing $f";
    jupyter nbconvert --to notebook --ExecutePreprocessor.kernel_name=${kernel_name} --execute ${pkg_dir}/notebooks/${f} --output-dir=./
done
```

### Building the site

May 2025 moving to use [`uv`](https://docs.astral.sh/uv/getting-started/installation/) to manage the python environment.


```sh
cd $HOME/src/swift-py-doc
uv venv .venv
```

```sh
cd $HOME/src/swift-py-doc
. .venv/bin/activate
uv pip install \
  mkdocs \
  mkdocs-material \
  mkdocstrings  \
  mkdocs-material-extensions \
  mkdocs-jupyter \
  mkdocstrings-python  \
  markdown-callouts \
  mkdocs-llmstxt
# May 2025 I am trying to produce llms.txt files
```

To test locally with `mkdocs serve`:

```sh
cd ${doc_dir}
mkdocs serve -w mkdocs.yml -w docs/
```

to build and deploy the site:

```bash
cd ${doc_dir}
mkdocs build --clean --site-dir _build/html --config-file mkdocs.yml
```

then, provided you have an ssh key set up for authentication with `github.com`:

```sh
mkdocs gh-deploy --clean --site-dir _build/html --config-file mkdocs.yml
```

### Examples as markdown

We can export the sample notebooks to markdown, with a view to use them as contexts for AI code aids.

**Note** that is important to **NOT** output to `${doc_dir}/docs/notebooks`, as it messes up the web site layout (see [issue 2](https://github.com/csiro-hydroinformatics/swift-py-doc/issues/1))

```sh
cd ${doc_dir}/docs/notebooks
out_dir=${doc_dir}/attic/docs/notebooks/
mkdir -p ${out_dir} 
for f in ${fn[@]} ; do
    echo "processing $f";
    jupyter nbconvert --to markdown ./${f} --output-dir=${out_dir} 
done
```

## Resources

Grateful for examplars for configuring `mkdocs`, at least as of 2023 or so:

* [https://github.com/FasterSpeeding/Tanjun/blob/master/mkdocs.yml](https://github.com/FasterSpeeding/Tanjun/blob/master/mkdocs.yml)
* [https://github.com/tiangolo/fastapi/blob/master/docs/en/mkdocs.yml](https://github.com/tiangolo/fastapi/blob/master/docs/en/mkdocs.yml)
