    server {
        listen 80;
        server_name your-domain.com www.your-domain.com;
        rewrite ^ https://$server_name$request_uri? permanent;
    }

    server {
        listen 443 ssl;
        server_name menu-api.com www.menu-api.com;
        server_tokens off;
        ssl_certificate /etc/nginx/ssl/menu-api.com.crt;
        ssl_certificate_key /etc/nginx/ssl/menu-api.com.key;
        ssl_session_cache shared:SSL:10m;
        ssl_session_timeout 10m;
        keepalive_timeout 70;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;
        ssl_stapling on;
        ssl_trusted_certificate /etc/nginx/ssl/ca.crt;
        access_log /var/log/nginx/menu-api.com.access.log;
        error_log /var/log/nginx/menu-api.com.su.error.log;


        location /admin {
            try_files $uri @proxy_api;
        }

        location @proxy_api {
            proxy_set_header X-Forwarded-Proto https;
            proxy_set_header X-Url-Scheme $scheme;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_pass   http://www.menu-api.com:8000;
        }

        location /static { alias /menu-manager-API/static; }

        location /media { alias /menu-manager-API/media; }

        location / {
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_pass http://www.menu-api.com:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Host $host;
        }
    }