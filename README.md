# YouTube Video Downloader

A simple, standalone application for downloading YouTube videos in the highest available quality. This application is packaged as an executable, so you don’t need to worry about installing Python or any additional libraries.

## Features

- Download YouTube videos in the highest quality available.
- Specify the directory where you want to save the downloaded videos.

## Downloading the Executable

1. **Visit the [Releases](https://github.com/ElCalvoYT/YT-Dowloader/releases) Page**:
   - Navigate to the Releases section of this repository to download the latest version of the executable.

2. **Download the ZIP File**:
   - Find the release version you want (e.g., `v1.0.0 - Initial Release`).
   - Download the ZIP file, which contains the executable and necessary files.

## Using the Executable

1. **Extract the ZIP File**:
   - Unzip the downloaded file to a directory of your choice.

2. **Run the Executable**:
   - Open a command prompt or terminal window.
   - Navigate to the directory where you extracted the ZIP file.

   ```bash
   cd path/to/extracted/zip
   ```

   - Run the executable with the following command:

   ```bash
   ./yt-downloader.exe <YouTube URL> <Output Directory>
   ```

   - Replace `<YouTube URL>` with the URL of the video you want to download.
   - Replace `<Output Directory>` with the path where you want to save the downloaded video.

   **Example**:

   ```bash
   ./yt-downloader.exe https://youtu.be/X2Njs8jv_yk .
   ```

   This command will download the video and save it in the current directory.

## Requirements

- No Python or additional libraries are required; everything is bundled in the executable.

## Troubleshooting

- **Executable Does Not Run**: Ensure you have the necessary permissions to execute the file. On Windows, you may need to unblock the file by right-clicking it, selecting "Properties," and then checking "Unblock" under the General tab.
- **Error Messages**: Ensure you are using the correct URL format and that the output directory exists or can be created.

## Contributing

If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
