# MyWebApp Docker Image

A simple, ultra-optimized web application built for Docker demonstration.

## Features
- Based on `nginx:alpine` for minimal footprint (~15MB)
- Security headers pre-configured (`X-Frame-Options`, `X-Content-Type-Options`)
- Built using layer reduction best practices

## Usage


docker run -d -p 8080:80 maazsheikh039/mywebapp:latest

