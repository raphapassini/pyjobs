var JobsList = React.createClass({displayName: "JobsList",
    getInitialState: function() {
        return {
            data: JobStore.getState(),
        }
    }

    , componentDidMount: function() {
        amplify.subscribe( 'JobStore.change', this._handleChange )
    }

    , render: function() {
        var job = {
            'title': 'Raphael',
            'desc': 'abc'
        }

        return (
            React.createElement(JobItem, {job: job})
        );
    }

    , _handleChange: function(data) {
        console.log(data)
    }
});

var JobItem = React.createClass({displayName: "JobItem",
    render: function() {
        return (
            React.createElement("div", {className: "panel panel-default"}, 
                React.createElement("div", {className: "panel-heading"}, this.props.job.title), 
                React.createElement("div", {className: "panel-body"}, 
                    this.props.job.desc
                )
            )
        )
    }
})