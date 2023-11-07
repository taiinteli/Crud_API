# Use a base image (e.g., Alpine Linux)
FROM alpine:latest

# Install SQLite
RUN apk --no-cache add sqlite

# Create a directory to store the SQLite database
RUN mkdir /data

# Define an entrypoint script
COPY ./init-db.sh /usr/local/bin/init-db.sh
RUN chmod +x /usr/local/bin/init-db.sh

# Set the entrypoint script to be executed
ENTRYPOINT ["init-db.sh"]

# Keep the container running
CMD ["tail", "-f", "/dev/null"]