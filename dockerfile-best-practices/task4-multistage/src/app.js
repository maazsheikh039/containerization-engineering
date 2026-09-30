const express = require('express');
const compression = require('compression');
const app = express();
const port = process.env.PORT || 3000;

app.use(compression());
app.get('/', (req, res) => res.json({ message: 'Multi-stage build demo', timestamp: new Date().toISOString() }));
app.get('/health', (req, res) => res.json({ status: 'healthy', uptime: process.uptime() }));
app.listen(port, '0.0.0.0', () => console.log(`Server on port ${port}`));
