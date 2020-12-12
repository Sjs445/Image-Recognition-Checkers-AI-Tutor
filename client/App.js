import React from 'react';
import { View, Image, Text, Button, StyleSheet } from 'react-native';
import ImagePicker from 'react-native-image-picker';
import axios from 'axios';

const styles = StyleSheet.create({
  checkersImage: {
    width: 400,
    height: 400
  }
});

export default class App extends React.Component { 
  state = {
    isLoading: false,
    apiRes: null,
    image: null
  }

  //  Choosing a Photo from Image Library
  handleChoosePhoto = () => {
    this.setState({
      image: null,
      apiRes: null
    })
    const options = {};
    ImagePicker.launchImageLibrary(options, response => {
      if(response.didCancel) {
        console.log('User cancelled image picker');
      }else if (response.error) {
        console.log('ImagePicker Error: ', response.error);
      } else if (response.customButton) {
        console.log('User tapped custom button: ', response.customButton);
      } else {
        this.setState({
          isLoading: true
        })
        // Send Post Request to backend with image bytes
        axios.post('https://checkerhelper.azurewebsites.net/api/GetNextMove?code=fxOtEGN8taKXKX2zJn1kwYqeVptGaFbVR7rz/ZFy8Gsew8AKOUKxAA==', {
          imageBytes: response.data
        })
        .then((res) => {
          // Do something with the API response
          console.log("API Response: " + res.data);
          this.setState({
            isLoading: false,
            apiRes: res.data,
            image: response
          })
        })
        .catch((err) => {
          console.log(err);
        });

      }
    });

  }

  //  Using camera to take the photo
  launchCamera = () => {
    let options = {
      storageOptions: {
        skipBackup: true,
        path: 'images',
      },
    };
    ImagePicker.launchCamera(options, (response) => {

      if (response.didCancel) {
        console.log('User cancelled image picker');
      } else if (response.error) {
        console.log('ImagePicker Error: ', response.error);
      } else if (response.customButton) {
        console.log('User tapped custom button: ', response.customButton);
        alert(response.customButton);
      } else {
        this.setState({
          isLoading: true
        })
        // Send Post Request to backend with image bytes
        axios.post('https://checkerhelper.azurewebsites.net/api/GetNextMove?code=fxOtEGN8taKXKX2zJn1kwYqeVptGaFbVR7rz/ZFy8Gsew8AKOUKxAA==', {
          imageBytes: response.data
        })
        .then((res) => {
          // Do something with the API response
          console.log("API Response: " + res.data);
          this.setState({
            isLoading: false,
            apiRes: res.data,
            image: response
          })
        })
        .catch((err) => {
          console.log(err);
        });
        // this.setState({
        //   filePath: response,
        //   fileData: response.data,
        //   fileUri: response.uri
        // });
      }
    });

  }

  render() {
    const { isLoading, apiRes, image } = this.state;
    return(
      <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
          {isLoading &&
          <Image style={styles.checkersImage} source={{uri: 'https://www.wpfaster.org/wp-content/uploads/2013/06/loading-gif.gif'}} />
          }

          {!apiRes && !isLoading &&
            <Image style={styles.checkersImage} source={{uri: 'https://www.freeimageslive.co.uk/files/images004/checkers.preview.jpg'}} />
          }

          {image &&
            <Image style={styles.checkersImage} source={{uri: image.uri}} />
          }

        <Text>
          Welcome to the checkers solver! Upload an image below and our AI will give you a suggested move.
        </Text>
        <Button 
          title="Choose Photo"
          onPress={this.handleChoosePhoto}
        />
        <Button
          title="Use Camera"
          onPress={this.launchCamera}
          disabled
        />
        {apiRes &&
          <Text>Our AI thinks you should do this move (Row of Piece, Column of Piece) (Row of Place to Move, Column of Place to Move): {apiRes}</Text>
        }
        
      </View>
    )
  }
};