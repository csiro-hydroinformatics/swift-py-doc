# swift-py-doc

swift python package documentation

## Dev notes

```bash
pkg_dir=${HOME}/src/swift/bindings/python/swift2
doc_dir=${HOME}/src/swift-py-doc

cd ${doc_dir}
rm -r docs
cp ${pkg_dir}/mkdocs.yml ${doc_dir}/
cp -r ${pkg_dir}/docs ${doc_dir}/
cp ${pkg_dir}/LICENSE.txt ${doc_dir}/docs/license.md


declare -a fn=(calibrate_multisite.ipynb \
  calibrate_subcatchments.ipynb \
  calibration_initial_states.ipynb \
  ensemble_model_runs.ipynb \
  error_correction_four_stages.ipynb \
  getting_started.ipynb \
  log_likelihood.ipynb \
  meta_parameters.ipynb \
  muskingum_multilink_calibration_explanation.ipynb \
  muskingum_multilink_calibration.ipynb \
  reservoir_geometry.ipynb)

mkdir -p ${doc_dir}/docs/notebooks

cd ${doc_dir}/docs/notebooks

for f in ${fn[@]} ; do
    echo "processing $f";
    jupyter nbconvert --to notebook --execute ${pkg_dir}/notebooks/${f} --output-dir=./
done
```

```bash
cd ${doc_dir}
mkdocs build --clean --site-dir _build/html --config-file mkdocs.yml
```

or testing with `mkdocs serve`

```sh
mkdocs gh-deploy --clean --site-dir _build/html --config-file mkdocs.yml
```
