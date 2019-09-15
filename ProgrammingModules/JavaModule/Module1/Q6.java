class M1Q6 {
	public static void main(String args[]){
		int largest = 0;
		int smallest = 0;
		int placeholder = 0;
		int[] intArr = {4,3,1,5};
		placeholder = intArr[0];
		for(int x : intArr) {
			for(int i = 0; i < intArr.length; i++){
				if(intArr[i]>placeholder){
					placeholder = intArr[i];
				}
			}
		}
		largest = placeholder;
		for(int i = 0; i < intArr.length; i++){
			for(int y = 0; y < intArr.length; y++){
				if(intArr[i] < intArr[y]){
					placeholder = intArr[i];
					for(int u : intArr) {
						if( u < placeholder){
							smallest = u;
						}
					}
				}
			}
		}
		System.out.println("The largest number is: " + largest + ", the smallest number is : " + smallest);
    }
}
