window.Pyjobs = Ember.Application.create();

Pyjobs.ApplicationAdapter = DS.RESTAdapter.extend({
    'namespace': 'api'
})
