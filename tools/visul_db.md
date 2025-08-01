# visualize_dataset

```
python lerobot/scripts/visualize_dataset.py --help
usage: visualize_dataset.py [-h] --repo-id REPO_ID --episode-index EPISODE_INDEX [--root ROOT]
                            [--output-dir OUTPUT_DIR] [--batch-size BATCH_SIZE]
                            [--num-workers NUM_WORKERS] [--mode MODE] [--web-port WEB_PORT]
                            [--ws-port WS_PORT] [--save SAVE] [--tolerance-s TOLERANCE_S]

options:
  -h, --help            show this help message and exit
  --repo-id REPO_ID     Name of hugging face repository containing a LeRobotDataset dataset (e.g.
                        `lerobot/pusht`).
  --episode-index EPISODE_INDEX
                        Episode to visualize.
  --root ROOT           Root directory for the dataset stored locally (e.g. `--root data`). By default,
                        the dataset will be loaded from hugging face cache folder, or downloaded from
                        the hub if available.
  --output-dir OUTPUT_DIR
                        Directory path to write a .rrd file when `--save 1` is set.
  --batch-size BATCH_SIZE
                        Batch size loaded by DataLoader.
  --num-workers NUM_WORKERS
                        Number of processes of Dataloader for loading the data.
  --mode MODE           Mode of viewing between 'local' or 'distant'. 'local' requires data to be on a
                        local machine. It spawns a viewer to visualize the data locally. 'distant'
                        creates a server on the distant machine where the data is stored. Visualize the
                        data by connecting to the server with `rerun ws://localhost:PORT` on the local
                        machine.
  --web-port WEB_PORT   Web port for rerun.io when `--mode distant` is set.
  --ws-port WS_PORT     Web socket port for rerun.io when `--mode distant` is set.
  --save SAVE           Save a .rrd file in the directory provided by `--output-dir`. It also
                        deactivates the spawning of a viewer. Visualize the data by running `rerun
                        path/to/file.rrd` on your local machine.
  --tolerance-s TOLERANCE_S
                        Tolerance in seconds used to ensure data timestamps respect the dataset fps
                        valueThis is argument passed to the constructor of LeRobotDataset and maps to
                        its tolerance_s constructor argumentIf not given, defaults to 1e-4.
```