from flask import Flask
import socket
import platform
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def container_info():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%H:%M:%S")
    python_version = platform.python_version()
    container_id = os.getenv('HOSTNAME', 'N/A')  # Common Docker env variable
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Container Response | DevOps Tool</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;600&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            :root {{
                --primary: #2563eb;
                --secondary: #1e40af;
                --accent: #3b82f6;
                --success: #10b981;
                --warning: #f59e0b;
                --danger: #ef4444;
                --dark: #1e293b;
                --light: #f8fafc;
                --gray: #64748b;
            }}
            
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                background-color: #0f172a;
                font-family: 'IBM Plex Mono', monospace;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: var(--light);
                overflow-x: hidden;
                line-height: 1.6;
            }}
            
            .terminal {{
                background: rgba(15, 23, 42, 0.8);
                border-radius: 12px;
                padding: 2.5rem;
                width: 90%;
                max-width: 800px;
                border: 1px solid rgba(56, 70, 101, 0.5);
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                position: relative;
                overflow: hidden;
            }}
            
            .terminal::before {{
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 40px;
                background: rgba(30, 41, 59, 0.5);
                border-top-left-radius: 12px;
                border-top-right-radius: 12px;
            }}
            
            .terminal-header {{
                display: flex;
                position: absolute;
                top: 12px;
                left: 15px;
            }}
            
            .terminal-btn {{
                width: 12px;
                height: 12px;
                border-radius: 50%;
                margin-right: 8px;
            }}
            
            .btn-red {{ background: var(--danger); }}
            .btn-yellow {{ background: var(--warning); }}
            .btn-green {{ background: var(--success); }}
            
            h1 {{
                font-family: 'JetBrains Mono', monospace;
                font-size: 1.8rem;
                margin-bottom: 1.5rem;
                color: var(--accent);
                position: relative;
                display: inline-block;
            }}
            
            h1::after {{
                content: '';
                position: absolute;
                bottom: -8px;
                left: 0;
                width: 60px;
                height: 3px;
                background: var(--accent);
                border-radius: 2px;
            }}
            
            .response-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1.5rem;
                margin: 2rem 0;
            }}
            
            .response-card {{
                background: rgba(30, 41, 59, 0.6);
                border-radius: 8px;
                padding: 1.2rem;
                border-left: 3px solid var(--accent);
                transition: all 0.3s ease;
            }}
            
            .response-card:hover {{
                transform: translateY(-3px);
                background: rgba(30, 41, 59, 0.8);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            }}
            
            .card-label {{
                font-size: 0.85rem;
                color: var(--gray);
                margin-bottom: 0.5rem;
                display: flex;
                align-items: center;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            
            .card-label i {{
                margin-right: 8px;
                font-size: 0.9rem;
            }}
            
            .card-value {{
                font-size: 1.1rem;
                font-weight: 500;
                font-family: 'JetBrains Mono', monospace;
                word-break: break-all;
            }}
            
            .hostname {{
                color: var(--accent);
            }}
            
            .time {{
                color: var(--success);
            }}
            
            .container-id {{
                color: var(--warning);
            }}
            
            .status-indicator {{
                display: inline-block;
                width: 10px;
                height: 10px;
                border-radius: 50%;
                background: var(--success);
                margin-right: 8px;
                animation: pulse 2s infinite;
            }}
            
            footer {{
                margin-top: 2.5rem;
                font-size: 0.85rem;
                color: var(--gray);
                border-top: 1px solid rgba(100, 116, 139, 0.3);
                padding-top: 1rem;
                display: flex;
                justify-content: space-between;
                flex-wrap: wrap;
            }}
            
            .deployed-by {{
                color: var(--accent);
                font-weight: 600;
            }}
            
            .request-count {{
                color: var(--warning);
            }}
            
            @keyframes pulse {{
                0% {{ opacity: 1; }}
                50% {{ opacity: 0.5; }}
                100% {{ opacity: 1; }}
            }}
            
            @media (max-width: 768px) {{
                .terminal {{
                    padding: 1.5rem;
                }}
                
                h1 {{
                    font-size: 1.5rem;
                }}
                
                .response-grid {{
                    grid-template-columns: 1fr;
                }}
            }}
            
            /* Terminal cursor effect */
            .typing {{
                border-right: 2px solid var(--accent);
                animation: blink 1s step-end infinite;
            }}
            
            @keyframes blink {{
                from, to {{ border-color: transparent; }}
                50% {{ border-color: var(--accent); }}
            }}
        </style>
    </head>
    <body>
        <div class="terminal">
            <div class="terminal-header">
                <div class="terminal-btn btn-red"></div>
                <div class="terminal-btn btn-yellow"></div>
                <div class="terminal-btn btn-green"></div>
            </div>
            
            <h1>container_response<span class="typing"></span></h1>
            <p>Response from Docker container instance</p>
            
            <div class="response-grid">
                <div class="response-card">
                    <div class="card-label"><i class="fas fa-server"></i> Hostname</div>
                    <div class="card-value hostname">{hostname}</div>
                </div>
                
                <div class="response-card">
                    <div class="card-label"><i class="fas fa-id-badge"></i> Container ID</div>
                    <div class="card-value container-id">{container_id}</div>
                </div>
                
                <div class="response-card">
                    <div class="card-label"><i class="fas fa-clock"></i> Current Time</div>
                    <div class="card-value time" id="live-time">{current_time}</div>
                </div>
                
                <div class="response-card">
                    <div class="card-label"><i class="fab fa-python"></i> Python Version</div>
                    <div class="card-value">{python_version}</div>
                </div>
                
                <div class="response-card">
                    <div class="card-label"><i class="fas fa-cube"></i> Platform</div>
                    <div class="card-value">{platform.system()} {platform.release()}</div>
                </div>
                
                <div class="response-card">
                    <div class="card-label"><i class="fas fa-heartbeat"></i> Status</div>
                    <div class="card-value"><span class="status-indicator"></span> Operational</div>
                </div>
            </div>
            
            <footer>
                <div>Deployed with <i class="fas fa-heart" style="color: var(--danger);"></i> by <span class="deployed-by">Kastro Kiran V</span></div>
                <div>Request served from: <span class="request-count">{hostname}</span></div>
            </footer>
        </div>
        
        <script>
            // Update time every second
            function updateTime() {{
                const now = new Date();
                document.getElementById('live-time').textContent = now.toLocaleTimeString();
            }}
            
            setInterval(updateTime, 1000);
            
            // Simulate typing effect
            const typingElement = document.querySelector('.typing');
            if (typingElement) {{
                let dots = '';
                setInterval(() => {{
                    dots = dots.length < 3 ? dots + '.' : '';
                    typingElement.textContent = dots;
                }}, 500);
            }}
            
            // Add terminal-like interaction
            document.addEventListener('keydown', (e) => {{
                if (e.ctrlKey && e.key === 'l') {{
                    e.preventDefault();
                    // This would normally clear the terminal
                    // For our demo, we'll just flash the screen
                    document.body.style.backgroundColor = 'rgba(59, 130, 246, 0.2)';
                    setTimeout(() => {{
                        document.body.style.backgroundColor = '#0f172a';
                    }}, 200);
                }}
            }});
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
