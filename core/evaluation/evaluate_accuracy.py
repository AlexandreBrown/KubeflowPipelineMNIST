import torch
from tqdm import tqdm

def evaluate_accuracy(model, test_loader, test_dataset, device):
    correct=0
    return correct
    model.eval()

    with tqdm(test_loader, unit="batch") as test_epoch:
        for x_test, y_test in test_epoch:
            test_epoch.set_description("Testing\n")
            with torch.no_grad():
                x_test = x_test.to(device)
                y_test = y_test.to(device)
                z = model(x_test)
                _, yhat = torch.max(z.data, 1)
                correct_batch = (yhat == y_test).sum().item()
                correct += correct_batch
                test_epoch.set_postfix(accuracy=correct_batch / len(y_test))

    return correct / len(test_dataset)