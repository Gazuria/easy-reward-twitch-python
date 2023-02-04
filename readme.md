<h1>Twitch Channel Points Custom Rewards Script</h1>

<p>Este script te permite interactuar con la API de Twitch para gestionar las recompensas personalizadas de tus puntos de canal.</p>

<h2>Requisitos</h2>
<ul>
  <li>Python 3.x</li>
  <li>requests (puedes instalarlo con <code>pip install requests</code>)</li>
</ul>

<h2>Configuración</h2>
<ol>
  <li>Obtén un <code>access_token</code> y un <code>client_id</code> de Twitch API en <a href="https://twitchtokengenerator.com/">Twitch Token Generator</a> generando el token con el permiso "channel:manage:redemptions".</li>
  <p>Una vez que tengas el <code>access_token</code>, <code>client_id</code> ponerlos en el config.py
  <p>Despues correr "pyhton broadcast.py" y poner el username para que se termine de configurar la app   
</ol>

<h2>Administrar Rewards</h2>
<ol>
  <li>Ejecutar <code>python manage.py</code> para crear, modificar rewards y borrar </li>
</ol>

<h2>Administrar Redeemptions</h2>
<ol>
  <li>Ejecutar <code>python canje.py</code> para ver los redeemtions 1 por 1 de cada reward</li>
</ol>

<h2>Notas</h2>
<p>Asegúrate de reemplazar <code>access_token</code>, <code>client_id</code> y <code>broadcaster_id</code> en el script con tus propios valores antes de ejecutarlo.</p>
<p>Una vez que tengas el <code>access_token</code>, <code>client_id</code> puedes ejecutar broadcaster.py para configurar el broadcaster_id
