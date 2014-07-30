Pyjobs.Router.map(function() {
  this.resource('jobs', { path: '/' });
});

Pyjobs.JobsRoute = Ember.Route.extend({
  model: function() {
    return this.store.find('job');
  }
});
