'use strict';

var React = require('react-native');
var Featured = require('./Featured');
var Search = require('./Search');

var {
    AppRegistry,
    TabBarIOS,
    Component
   } = React;

class Thiruvachanam extends Component {

    constructor(props) {
        super(props);
        this.state = {
            selectedTab: 'featured'
        };
    }

    render() {
        return (
          <Featured/>
        );
    }
}

AppRegistry.registerComponent('Thiruvachanam', () => Thiruvachanam);
