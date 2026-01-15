#!/usr/bin/env python3
"""
LLM Benchmark Demos Launcher
A GUI application to launch and view the classic LLM coding benchmark demos.

Built using the Specify-Flow paradigm - demonstrating one-shot code generation
for classic visual/interactive challenges.
"""

import os
import sys
import webbrowser
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import http.server
import socketserver
import threading

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.resolve()

# Demo definitions
DEMOS = [
    {
        "id": "01-bouncing-polyhedron",
        "title": "Bouncing Ball in Rotating Polyhedron",
        "description": "Physics simulation with real-time 3D collision detection. A ball bounces inside a rotating icosahedron, changing color on each impact.",
        "tags": ["3D", "Physics", "Collision Detection"],
        "color": "#00d4ff"
    },
    {
        "id": "02-dvd-logo",
        "title": "DVD Logo Bounce",
        "description": "The classic screensaver! Watch the DVD logo bounce around, changing colors. Count bounces and celebrate when it hits a corner!",
        "tags": ["Animation", "Nostalgia", "Simple Physics"],
        "color": "#ff0000"
    },
    {
        "id": "03-game-of-life",
        "title": "Conway's Game of Life",
        "description": "Cellular automaton simulation. Click to draw cells, add patterns like gliders and glider guns, and watch life evolve.",
        "tags": ["Cellular Automaton", "Interactive", "Simulation"],
        "color": "#00ff66"
    },
    {
        "id": "04-rotating-cube",
        "title": "3D Rotating Cube",
        "description": "A 3D cube with perspective projection. Multiple rendering styles (neon, wireframe, solid, rainbow). Drag to rotate, scroll to zoom.",
        "tags": ["3D", "Perspective", "Interactive"],
        "color": "#ff00ff"
    },
    {
        "id": "05-particle-system",
        "title": "Particle System & Fireworks",
        "description": "Dynamic particle effects with multiple styles: fireworks, fountains, spirals, explosions, and rain. Click anywhere to launch!",
        "tags": ["Particles", "Animation", "Effects"],
        "color": "#ff8800"
    }
]

class LocalServer:
    """Simple HTTP server to serve the demos locally."""

    def __init__(self, port=8765):
        self.port = port
        self.server = None
        self.thread = None

    def start(self):
        """Start the local server in a background thread."""
        os.chdir(SCRIPT_DIR)

        handler = http.server.SimpleHTTPRequestHandler
        handler.log_message = lambda *args: None  # Suppress logging

        try:
            self.server = socketserver.TCPServer(("", self.port), handler)
            self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            self.thread.start()
            return True
        except OSError:
            # Port might be in use, try another
            self.port += 1
            return self.start() if self.port < 8800 else False

    def stop(self):
        """Stop the server."""
        if self.server:
            self.server.shutdown()

    def get_url(self, demo_id):
        """Get the URL for a specific demo."""
        return f"http://localhost:{self.port}/{demo_id}/index.html"


class DemoLauncher(tk.Tk):
    """Main GUI application for launching demos."""

    def __init__(self):
        super().__init__()

        self.title("LLM Benchmark Demos")
        self.geometry("800x650")
        self.configure(bg="#1a1a2e")

        # Start local server
        self.server = LocalServer()
        if not self.server.start():
            self.show_error("Could not start local server")

        self.create_widgets()

        # Handle window close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        """Create all GUI widgets."""

        # Title
        title_frame = tk.Frame(self, bg="#1a1a2e")
        title_frame.pack(fill=tk.X, pady=20)

        title = tk.Label(
            title_frame,
            text="LLM Benchmark Demos",
            font=("Segoe UI", 24, "bold"),
            fg="#ffffff",
            bg="#1a1a2e"
        )
        title.pack()

        subtitle = tk.Label(
            title_frame,
            text="Classic coding challenges - one-shot generation via Specify-Flow",
            font=("Segoe UI", 11),
            fg="#888888",
            bg="#1a1a2e"
        )
        subtitle.pack()

        # Demos container
        demos_frame = tk.Frame(self, bg="#1a1a2e")
        demos_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        for i, demo in enumerate(DEMOS):
            self.create_demo_card(demos_frame, demo, i)

        # Footer
        footer = tk.Frame(self, bg="#1a1a2e")
        footer.pack(fill=tk.X, pady=15)

        # Launch All button
        launch_all_btn = tk.Button(
            footer,
            text="Launch All Demos",
            font=("Segoe UI", 11, "bold"),
            fg="#ffffff",
            bg="#4a4a6e",
            activebackground="#5a5a7e",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.launch_all
        )
        launch_all_btn.pack()

        # Server info
        server_info = tk.Label(
            footer,
            text=f"Local server running on port {self.server.port}",
            font=("Segoe UI", 9),
            fg="#666666",
            bg="#1a1a2e"
        )
        server_info.pack(pady=(10, 0))

    def create_demo_card(self, parent, demo, index):
        """Create a card widget for a demo."""

        card = tk.Frame(
            parent,
            bg="#2a2a4e",
            highlightbackground=demo["color"],
            highlightthickness=2,
            padx=15,
            pady=12
        )
        card.pack(fill=tk.X, pady=8)

        # Left side - info
        info_frame = tk.Frame(card, bg="#2a2a4e")
        info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Title
        title = tk.Label(
            info_frame,
            text=f"{index + 1}. {demo['title']}",
            font=("Segoe UI", 13, "bold"),
            fg=demo["color"],
            bg="#2a2a4e",
            anchor="w"
        )
        title.pack(fill=tk.X)

        # Description
        desc = tk.Label(
            info_frame,
            text=demo["description"],
            font=("Segoe UI", 10),
            fg="#cccccc",
            bg="#2a2a4e",
            anchor="w",
            wraplength=500,
            justify=tk.LEFT
        )
        desc.pack(fill=tk.X, pady=(5, 0))

        # Tags
        tags_text = " | ".join(demo["tags"])
        tags = tk.Label(
            info_frame,
            text=tags_text,
            font=("Segoe UI", 9),
            fg="#888888",
            bg="#2a2a4e",
            anchor="w"
        )
        tags.pack(fill=tk.X, pady=(3, 0))

        # Right side - button
        btn_frame = tk.Frame(card, bg="#2a2a4e")
        btn_frame.pack(side=tk.RIGHT, padx=(20, 0))

        launch_btn = tk.Button(
            btn_frame,
            text="Launch",
            font=("Segoe UI", 10, "bold"),
            fg="#ffffff",
            bg=demo["color"],
            activebackground=demo["color"],
            activeforeground="#ffffff",
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2",
            command=lambda d=demo: self.launch_demo(d)
        )
        launch_btn.pack()

    def launch_demo(self, demo):
        """Launch a single demo in the browser."""
        url = self.server.get_url(demo["id"])
        webbrowser.open(url)

    def launch_all(self):
        """Launch all demos in the browser."""
        for demo in DEMOS:
            self.launch_demo(demo)

    def show_error(self, message):
        """Show an error message."""
        from tkinter import messagebox
        messagebox.showerror("Error", message)

    def on_close(self):
        """Handle window close event."""
        self.server.stop()
        self.destroy()


def main():
    """Main entry point."""
    app = DemoLauncher()
    app.mainloop()


if __name__ == "__main__":
    main()
