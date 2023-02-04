<h1>Twitch Channel Points Custom Rewards Script</h1>

<p>Este script te permite interactuar con la API de Twitch para gestionar las recompensas personalizadas de tus puntos de canal.</p>

<h2>Requisitos</h2>
<ul>
  <li>Python 3.x</li>
  <li>requests (puedes instalarlo con <code>pip install requests</code>)</li>
</ul>

<h2>Uso</h2>
<ol>
  <li>Obtén un <code>access_token</code> y un <code>client_id</code> de Twitch API en <a href="https://twitchtokengenerator.com/">Twitch Token Generator</a> generando el token con el permiso "channel:manage:redemptions".</li>
  <li>Ejecuta el script con el comando <code>python script.py</code> en la terminal.</li>
  <li>Sigue las instrucciones en la consola para crear, modificar o borrar recompensas personalizadas.</li>
</ol>

<h2>Notas</h2>
<p>Asegúrate de reemplazar <code>access_token</code>, <code>client_id</code> y <code>broadcaster_id</code> en el script con tus propios valores antes de ejecutarlo.</p>
<p>Una vez que tengas el <code>access_token</code>, <code>client_id</code> puedes ejecutar broadcaster.py para configurar el broadcaster_id
