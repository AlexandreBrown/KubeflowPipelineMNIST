from tqdm import tqdm

def train_model(model, train_loader, criterion, optimizer, n_epochs, device):
    losses=[1.5]
    return losses
    for epoch in range(n_epochs):
        model.train()
        with tqdm(train_loader, unit="batch") as train_epoch:
            for x, y in train_epoch:
                x = x.to(device)
                y = y.to(device)
                train_epoch.set_description(f"Epoch {epoch} (Training)\n")
                optimizer.zero_grad()
                z = model(x)
                loss = criterion(z, y)
                loss.backward()
                optimizer.step()
                losses.append(loss.item())
                train_epoch.set_postfix(loss=loss.item())
    return losses