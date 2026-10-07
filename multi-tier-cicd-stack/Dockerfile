FROM python:3.9-alpine

RUN addgroup -g 1001 -S appuser && adduser -u 1001 -S appuser -G appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
RUN chown -R appuser:appuser /app

USER appuser
EXPOSE 5000

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:5000/health || exit 1

CMD ["python", "app.py"]
