'use strict';

var REQUEST_URL = 'https://www.googleapis.com/books/v1/volumes?q=subject:fiction';

var React = require('react-native');
var BookDetail = require('./BookDetail');

var {
  Image,
  StyleSheet,
  Text,
  View,
  Component,
  ListView,
  TouchableHighlight,
  ActivityIndicatorIOS
} = React;


var styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5FCFF',
    alignItems: 'stretch'
  },
  thumbnail: {
    width: 53,
    height: 81,
    marginRight: 10
  },
  rightContainer: {
    flex: 1
  },
  title: {
    fontSize: 20,
  },
  author: {
    color: '#656565'
  },
  separator: {
    height: 1,
    backgroundColor: '#dddddd'
  },
  listView: {
    backgroundColor: '#F5FCFF'
  },
  loading: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center'
  }
});

class BookList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
      dataSource: new ListView.DataSource({
        rowHasChanged: (row1, row2) => row1 !== row2
      })
    };
  }

  componentDidMount() {
    this.fetchData();
  }

  fetchData() {
    fetch(REQUEST_URL)
    .then((response) => response.json())
    .then((responseData) => {
      this.setState({
        dataSource: this.state.dataSource.cloneWithRows(responseData.items),
        isLoading: false
      });
    })
    .done();
  }

  render() {
    if (this.state.isLoading) {
      return this.renderLoadingView();
    }

    return (
      <ListView
      dataSource={this.state.dataSource}
      renderRow={this.renderBook.bind(this)}
      style={styles.listView}
      automaticallyAdjustContentInsets={false}
      />
    );
  }  

  renderLoadingView() {
    return (
      <View style={styles.loading}>
      <ActivityIndicatorIOS
      size='large'/>
      <Text>
      Loading books...
        </Text>
      </View>
    );
  }
  renderBook(book) {
    return (
      <TouchableHighlight onPress={() => this.showBookDetail(book)}  underlayColor='#dddddd'> 
        <View>
            <View style={styles.container}>
              <Text style={styles.title}>{book.volumeInfo.title}</Text>
            </View>
          <View style={styles.separator} />
        </View>
      </TouchableHighlight>
    );
  }

  showBookDetail(book) {
    this.props.sharedNav.push({
      title: book.volumeInfo.title,
      component: BookDetail,
      passProps: {book}
    });
  }

}

BookList.contextTypes =  {
  sharedNavigator: React.PropTypes.any
}

module.exports = BookList;
