FROM alpine:3.12
ENV SSH_AUTH_SOCK /app/ssh-agent.sock
ENV SSH_KEY_PATH ""

RUN mkdir -p /app && apk add --no-cache openssh-client

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
HEALTHCHECK --interval=5s --timeout=3s --retries=3 CMD test -S $SSH_AUTH_SOCK
