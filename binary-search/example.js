// Nodejs 18.12.0

function binarySearch(arr, item) {
	let low = 0
	let high = arr.length - 1

	while (low <= high) {
		let mid = Math.floor((low + high) / 2)

		if (arr[mid] === item) {
			return mid
		}

		if (arr[mid] > item) {
			high = mid - 1
		} else {
			low = mid + 1
		}

	}

	return null
}

const arr = [1, 3, 5, 7, 9]

console.log(binarySearch(arr, 3)) // output 1
console.log(binarySearch(arr, -1)) // output null