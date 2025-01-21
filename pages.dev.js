export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname.startsWith('/static/')) {
      return env.ASSETS.fetch(request);
    }
    return env.FLASK.fetch(request);
  }
}
