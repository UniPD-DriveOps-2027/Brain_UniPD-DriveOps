<!-- Purpose: Document files that cannot safely contain embedded comments. Inputs: repository binary/strict-format inventory. Outputs: purpose and I/O reference without altering runtime bytes. -->

# Binary and strict-format file index

Python, launch, configuration, interface, build, and plain-text data files carry
`Purpose`, `Inputs`, and `Outputs` headers directly. The files below cannot safely
accept such headers: adding text would corrupt a binary or violate its strict
format. Their documentation therefore lives here.

## Brain map data

| File | Purpose | Inputs | Outputs / consumer |
|---|---|---|---|
| `src/brain_core/brain_core/assets/data/2024_VerySmall.png` | 5338×3541 RGB track-map image and graph coordinate reference. | Track artwork; no runtime arguments. | OpenCV map background used by `brain_io.runner` and route visualisation. |

## ONNX perception models

| File | Purpose | Inputs | Outputs / consumer |
|---|---|---|---|
| `lane_keeper_small.onnx` | Estimate normal-lane lateral and heading errors. | Bottom camera region converted to grayscale/Canny and resized to a 32×32 OpenCV DNN blob. | `e2` lateral error and `e3` heading error consumed by legacy camera lane following. |
| `lane_keeper_ahead.onnx` | Estimate the forward lane heading for speed/no-lane behaviour. | Preprocessed 32×32 grayscale edge image. | Forward `e3` heading estimate and visual target point. |
| `he_left.onnx` | Predict steering heading through a left intersection. | Preprocessed 32×32 grayscale edge image. | Intersection heading error for the legacy special-path controller. |
| `he_right.onnx` | Predict steering heading through right intersections and selected roundabout phases. | Preprocessed 32×32 grayscale edge image. | Intersection/roundabout heading error. |
| `he_straight.onnx` | Predict steering heading through a straight intersection. | Original and mirrored preprocessed 32×32 edge images. | Symmetry-corrected forward heading error. |
| `about_dif.onnx` | Predict steering heading while travelling around a roundabout. | Preprocessed 32×32 grayscale edge image. | Roundabout heading error. |
| `stopline_estimator.onnx` | Preserve the original stop-line regression model. | Preprocessed camera edge image. | Legacy stop-line estimate; loaded for compatibility but the advanced model is active. |
| `stopline_estimator_advanced.onnx` | Regress stop-line geometry. | Lower camera image, blurred/Canny processed, then resized to a 32×32 DNN blob. | Stop-line forward distance, lateral position, and angle. |
| `sign_yolo.onnx` | Detect nine traffic-sign classes for the OAK-D node. | Letterboxed RGB camera tensor, normally 640×640. | Bounding boxes, class scores, and confidences used for `/traffic/*` topics. |

All ONNX paths above are relative to
`src/brain_core/brain_core/assets/models/`.

## Pickled classical perception models

| File | Purpose | Inputs | Outputs / consumer |
|---|---|---|---|
| `traffic_signs_models/kmeans_linear_100.pkl` | Quantise 128-dimensional local sign descriptors into 100 visual words. | Descriptor matrix from a candidate sign crop. | Visual-word assignments used to build the sign histogram. |
| `traffic_signs_models/scale_linear_100.pkl` | Standardise the 100-element sign histogram. | Sign visual-word histogram. | Scaled feature vector for the sign SVM. |
| `traffic_signs_models/svm_linear_100.pkl` | Classify traffic signs into nine legacy classes. | Scaled 100-element sign feature vector. | Integer sign class prediction. |
| `obstacle_models/kmeans_linear_1200.pkl` | Quantise 128-dimensional obstacle descriptors into 1200 visual words. | Descriptor matrix from an obstacle crop. | Visual-word assignments used to build the obstacle histogram. |
| `obstacle_models/scale_linear_1200.pkl` | Standardise the 1200-element obstacle histogram. | Obstacle visual-word histogram. | Scaled feature vector for the obstacle SVM. |
| `obstacle_models/svm_linear_1200.pkl` | Classify car, pedestrian, or roadblock obstacles. | Scaled 1200-element obstacle feature vector. | Class ID `0`, `1`, or `2`. |

The pickle models were created with scikit-learn 1.0.2. Loading them with a
different scikit-learn version can produce compatibility warnings.

## V2X strict files

| File | Purpose | Inputs | Outputs / consumer |
|---|---|---|---|
| `src/brain_io/brain_io/inputs/v2x/TrafficCommunication/useful/publickey_server.pem` | Public key for validating production traffic-server communication. | PEM-encoded RSA public key bytes. | Cryptographic public-key object used by the active V2X bridge. |

## ROS package resource markers

| File | Purpose | Inputs | Outputs / consumer |
|---|---|---|---|
| `src/brain_core/resource/brain_core` | Register the package name in the ament resource index. | File presence during installation. | ROS 2 package discovery entry for `brain_core`. |
| `src/brain_io/resource/brain_io` | Register the package name in the ament resource index. | File presence during installation. | ROS 2 package discovery entry for `brain_io`. |

These marker files intentionally remain empty.

## Isolated SPARCS/Vicon binary fixtures

All paths below are relative to `testing/sparcs_vicon/legacy/` and are retained
only for independent coordinate tests.

| File | Purpose | Inputs | Outputs / consumer |
|---|---|---|---|
| `sparcs_path.npy` | Base legacy SPARCS reference path. | NumPy coordinate array produced by the path-generation tool. | Loaded reference coordinates for SPARCS/Vicon tests. |
| `sparcs_path_precise.npy` | Higher-precision base SPARCS path. | NumPy coordinate array. | Precise reference coordinates for tests. |
| `sparcs_path_ext.npy` | Exterior-loop SPARCS path. | NumPy coordinate array. | Exterior test route. |
| `sparcs_path_ext_precise.npy` | Higher-precision exterior-loop path. | NumPy coordinate array. | Precise exterior test route. |
| `sparcs_path_int.npy` | Interior-loop SPARCS path. | NumPy coordinate array. | Interior test route. |
| `sparcs_path_int_precise.npy` | Higher-precision interior-loop path. | NumPy coordinate array. | Precise interior test route. |
| `test_Medium_old.png` | Legacy medium-resolution SPARCS track image. | Stored map pixels. | Visual background for legacy coordinate tests. |
| `test_Small.png` | Small SPARCS track image. | Stored map pixels. | Visual background for legacy coordinate tests. |
| `test_VerySmall.png` | Very-small SPARCS track image. | Stored map pixels. | Visual background for legacy coordinate tests. |
| `test_VerySmall_old.png` | Older very-small SPARCS track image. | Stored map pixels. | Historical comparison fixture. |
