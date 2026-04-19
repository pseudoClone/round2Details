# Simple Application

- This application does name calling along with age

## Build
Ensure you have the latest docker buildx installed.

`sudo pacman -S docker-buildx`

`sudo apt-get install docker-buildx`
- Jump to the application directory and execute:

```bash
docker buildx build -t simple-app .
```