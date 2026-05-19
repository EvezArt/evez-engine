# EVEZ Alt-Stack: Free Open Source Alternatives

## Database
- PostgreSQL 17 (replace Supabase)
- pgvector for embeddings
- Backup: pgBackRest + WAL-G

## Backup  
- Restic to S3/R2
- BorgBase for offsite
- Daily snapshots retained 30 days

## API Gateway  
- Traefik + Authelia
- Kong for rate limiting
- OpenAPI-first design

## Monitoring
- Prometheus + Grafana LGTM stack
- Uptime Kuma for status pages
- OpenTelemetry tracing

Built with: docker-compose -f docker-compose.alt.yml up -d
