#!/usr/bin/env python3
import streamlit as st
import os
import deepzoom
import streamlit.components.v1 as components


st.set_page_config(
   page_title="Streamlit iCodeIdoia",
   page_icon="images/icon.png",layout="wide",initial_sidebar_state="expanded"
)

st.image("images/banner.jpg")

def view_slide():
 components.html("""
 <div id="container" class="m_image_slider__viewer">
    <div class="m_image_slider__handle">
      <div class="m_image-slider__handle__divider"></div>
      <div class="m_image-slider__handle__circle">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path fill="#FFF" d="M13 21l-5-5 5-5m6 0l5 5-5 5"/></svg>
      </div>
    </div>
 </div>  
 <script type="text/javascript">
 // Proof of concept by Illya Moskvin
 // v1 - 2016 - IMA Lab, Indianapolis Museum of Art
 // v2 - 2021 - Experience Design, Art Institute of Chicago
 // MIT License
 // This example was updated in 2021 to not require jQuery.

 const viewerElement = document.getElementById('container');
 const handleElement = viewerElement.querySelector('.m_image_slider__handle');

 const imageData = {
    "leftImage": "https://raw.githubusercontent.com/webdevserv/images_video/main/old/left/info.json",
    "rightImage": "https://raw.githubusercontent.com/webdevserv/images_video/main/old/right/info.json",
    "isSliderZoomable": true,
 };

 let viewer;
 let middle;

 let leftImage = null;
 let rightImage = null;

 let leftRect = new OpenSeadragon.Rect(0,0,0,0);
 let rightRect = new OpenSeadragon.Rect(0,0,0,0);

 let oldSpringX = 0.5;

 initViewer();
 function initViewer() {
  viewer = OpenSeadragon({
    element: viewerElement,
    xmlns: 'http://schemas.microsoft.com/deepzoom/2008',
    prefixUrl: '//openseadragon.github.io/openseadragon/images/',
    zoomPerClick: imageData.isSliderZoomable ? 1.3 : 1, // 2.0
    showZoomControl: imageData.isSliderZoomable,
    showFullPageControl: true,
    showRotationControl: false,
    showSequenceControl: false,
  });

  middle = new OpenSeadragon.Point(viewerElement.clientWidth / 2, viewerElement.clientHeight / 2);

  viewer.addHandler('animation-start', imagesClip);
  viewer.addHandler('animation', imagesClipAggressive);

  viewer.addTiledImage({
    tileSource: imageData.leftImage,
    success: function(event) {
      leftImage = event.item;
      imagesLoaded();
    }
  });

  viewer.addTiledImage({
    tileSource: imageData.rightImage,
    success: function(event) {
      rightImage = event.item;
      imagesLoaded();
    }
  });
 }

 function updateMiddle(offset) {
  middle.x = offset;
 }

 function imagesLoaded() {
  if (leftImage && rightImage) {
    leftRect.height = leftImage.getContentSize().y;
    rightRect.height = rightImage.getContentSize().y;
    imagesClip();
    initClip();
  }
 }

 function imagesClip() {
  let rox = rightImage.viewerElementToImageCoordinates(middle).x;
  let lox = leftImage.viewerElementToImageCoordinates(middle).x;

  rightRect.x = rox;
  rightRect.width = rightImage.getContentSize().x - rox;

  leftRect.width = lox;

  leftImage.setClip(leftRect);
  rightImage.setClip(rightRect);
 }

 function imagesClipAggressive() {
  if (!rightImage || !leftImage) {
    window.setTimeout(imagesClipAggressive, 200);
    return;
  }

  let newSpringX = viewer.viewport.centerSpringX.current.value;
  let deltaSpringX = newSpringX - oldSpringX;
  oldSpringX = newSpringX;

  let fixedMiddle = viewer.viewport.viewerElementToViewportCoordinates(middle);
  fixedMiddle.x += deltaSpringX;

  let rox = rightImage.viewportToImageCoordinates(fixedMiddle).x;
  let lox = leftImage.viewportToImageCoordinates(fixedMiddle).x;

  imagesClipShared(rox, lox);
 }

 function imagesClip() {
  if (!rightImage || !leftImage) {
    window.setTimeout(imagesClip, 200);
    return;
  }

  let rox = rightImage.viewerElementToImageCoordinates(middle).x;
  let lox = leftImage.viewerElementToImageCoordinates(middle).x;

  imagesClipShared(rox, lox);
 }

 function imagesClipShared(rox, lox) {
  rightRect.x = rox ;
  rightRect.width = rightImage.getContentSize().x - rox;

  leftRect.width = lox;

  leftImage.setClip(leftRect);
  rightImage.setClip(rightRect);
 }

 function initClip() {
  // We will assume that the width of the handle element does not change
  let dragWidth = handleElement.offsetWidth;

  // However, we will track when the container resizes
  let containerWidth, containerOffset, minLeft, maxLeft;

  function updateContainerDimensions() {
    containerWidth = viewerElement.offsetWidth;
    containerOffset = viewerElement.getBoundingClientRect().left + window.scrollX;
    minLeft = containerOffset + 10;
    maxLeft = containerOffset + containerWidth - dragWidth - 10;

    // Spoof the mouse events
    let offset = handleElement.getBoundingClientRect().left + window.scrollX + dragWidth / 2;
    let event;

    // Bind the drag event
    event = new Event('mousedown');
    event.pageX = offset;

    handleElement.dispatchEvent(event);

    // Execute the drag event
    event = new Event('mousemove');
    event.pageX = offset;

    viewerElement.dispatchEvent(event);

    // Unbind the drag event
    handleElement.dispatchEvent(new Event('mouseup'));
  }

  // Retrieve initial container dimention
  updateContainerDimensions();

  // Bind the container resize
  window.addEventListener('resize', updateContainerDimensions);

  function handleTouchStart(event) {
    handleStartShared(event.targetTouches[0].pageX);
  }

  function handleMouseDown(event) {
    handleStartShared(event.pageX);
  }

  function handleStartShared(pageX) {
    let xPosition = handleElement.getBoundingClientRect().left + window.scrollX + dragWidth - pageX;

    function trackDragMouse(event) {
      trackDragShared(event.pageX);
    }

    function trackDragTouch(event) {
      trackDragShared(event.changedTouches[0].pageX);
    }

    function trackDragShared(pageX) {
      let leftValue = pageX + xPosition - dragWidth;

      // Constrain the draggable element to move inside its container
      leftValue = Math.max(leftValue, minLeft);
      leftValue = Math.min(leftValue, maxLeft);

      let widthPixel = (leftValue + dragWidth/2 - containerOffset);
      let widthFraction = widthPixel/containerWidth;
      let widthPercent = widthFraction*100+'%';

      handleElement.style.left = widthPercent;

      updateMiddle(widthPixel);
      imagesClip();
    }

    viewerElement.addEventListener('mousemove', trackDragMouse);
    viewerElement.addEventListener('touchmove', trackDragTouch);

    function unbindTrackDrag(event) {
      viewerElement.removeEventListener('mousemove', trackDragMouse);
      viewerElement.removeEventListener('touchmove', trackDragTouch);
    }

    document.addEventListener('mouseup', unbindTrackDrag, {once: true});
    document.addEventListener('touchend', unbindTrackDrag, {once: true});

    event.preventDefault();
  }

  handleElement.addEventListener('mousedown', handleMouseDown);
  handleElement.addEventListener('touchstart', handleTouchStart);
 }
 </script>    
 <style>

 html, body {
	height: 100%;
  margin: 0;
  padding: 0;
 }

 .m_image_slider__viewer {
  height: 100%;
  width: 100%;
  position: relative;
  overflow: hidden;
 }

 .m_image_slider__handle {
  position: absolute;

  /* center the element */
  left: 50%;
  top: 50%;
 }

 /* overflow is hidden by .m_image_slider__viewer */
 .m_image_slider__handle__divider {
  position: absolute;
  left: 50%;
  top: 50%;
  background-color: white;
  width: 3px;
  height: 150vh;
  transform: translate(-50%, -50%);
  z-index: 2;
 }

 .m_image_slider__handle__circle {
  position: absolute;

  height: 45px;
  width: 45px;

  /* center the element */
  left: 50%;
  top: 50%;

  margin-left: -23px;
  margin-top: -23px;

  border-radius: 50%;

  background: gray !important;
  cursor: move;

  box-shadow: 0 0 0 6px rgba(0, 0, 0, 0.2), 0 0 10px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.3);
  z-index: 3;
 }

 .m_image_slider__handle svg {
  display: block;
  margin-left: auto;
  margin-right: auto;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
 }
 </style>
 """,
 height=600,
 )
               
def main():      
# ---- TABS ----
 tab1, tab2 = st.tabs(["Slider","cccccccccc"])
 with tab1:     
  st.subheader("OpenSeadDragon deepzoom viewer")
  img_description = st.text('Instructions: Top small window, move around the slide by dragging, and use the mouse wheel to zoom.')
  view_slide()
  #eskuz; change dzi content to "Format":"jpg","Overlap":"2",TileSize":"256","Size":{"Height": "9221","Width":"7026"}
  st.caption("Special thanks for openseadragon viewer; https://github.com/openseadragon")
  
 with tab2:
  st.subheader("Deepzoom image creator (dzi)")
        
                 
if __name__ == "__main__":
   main()